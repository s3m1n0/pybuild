from .arguments import parse_args


def main(argv: str | None = None) -> int:
    args = parse_args(argv)

    if args.command == "build":
        print(f"Building site from {args.input_dir!r} to {args.output_dir!r}")
    elif args.command == "init":
        print(f"Initializing {args.name!r} using the {args.template!r} template")
    elif args.command == "serve":
        print(f"Serving site on http://{args.host}:{args.port}")

    return 0
