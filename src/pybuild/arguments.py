import argparse
from typing import Literal, cast


class BuildArgs(argparse.Namespace):
    command: Literal["build"]
    input_dir: str
    output_dir: str
    clean: bool


class InitArgs(argparse.Namespace):
    command: Literal["init"]
    name: str
    template: str


class ServeArgs(argparse.Namespace):
    command: Literal["serve"]
    host: str
    port: int


type CLIArgs = BuildArgs | InitArgs | ServeArgs


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
        type=str,
        default=".",
        help="Directory containing site content and templates",
    )
    build.add_argument(
        "--output-dir",
        type=str,
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
    init.add_argument(
        "name",
        type=str,
        help="Name of the site project or target directory",
    )
    init.add_argument(
        "--template",
        type=str,
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
        "--host",
        type=str,
        default="127.0.0.1",
        help="Host interface to bind the server to",
    )
    serve.add_argument(
        "--port", type=int, default=8000, help="Port to serve the site on"
    )

    return parser


def parse_args(argv: str | None = None) -> CLIArgs:
    parser = build_parser()
    args = cast(CLIArgs, parser.parse_args(argv))

    if args.command == "build":
        return cast(BuildArgs, args)
    if args.command == "init":
        return cast(InitArgs, args)
    if args.command == "serve":
        return cast(ServeArgs, args)

    raise ValueError(f"Unsupported command: {args.command!r}")
