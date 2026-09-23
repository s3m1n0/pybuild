import argparse
from collections.abc import Sequence


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="pybuild",
        description="Build static websites from content, templates, and assets.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    build = subparsers.add_parser(
        "build",
        help="build a static site",
        description="Generate a static site from the source directory.",
    )
    build.add_argument(
        "--input-dir",
        default=".",
        help="Directory containing site content and templates",
    )
    build.add_argument(
        "--output-dir",
        default="_site",
        help="Directory where the generated site should be written",
    )
    build.add_argument(
        "--clean",
        action="store_true",
        help="Remove the output directory before generating the site",
    )

    init = subparsers.add_parser(
        "init",
        help="create a new site scaffold",
        description="Create a new static site project in a directory.",
    )
    init.add_argument("name", help="Name of the site project or target directory")
    init.add_argument(
        "--template",
        choices=("minimal", "blog", "docs"),
        default="minimal",
        help="Template to scaffold for the new site",
    )

    serve = subparsers.add_parser(
        "serve",
        help="serve the built site locally",
        description="Serve the generated site with a local development server.",
    )
    serve.add_argument(
        "--host", default="127.0.0.1", help="Host interface to bind the server to"
    )
    serve.add_argument(
        "--port", type=int, default=8000, help="Port to serve the site on"
    )

    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "build":
        print(f"Building site from {args.source!r} to {args.output_dir!r}")
    elif args.command == "init":
        print(f"Initializing {args.name!r} using the {args.template!r} template")
    elif args.command == "serve":
        print(f"Serving site on http://{args.host}:{args.port}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
