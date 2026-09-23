import argparse

from pybuild import build_parser


def test_build_parser_accepts_build_command() -> None:
    parser = build_parser()

    args = parser.parse_args(["build", "content", "--output-dir", "dist"])

    assert args.command == "build"
    assert args.source == "content"
    assert args.output_dir == "dist"
    assert args.clean is False


def test_build_parser_accepts_init_command() -> None:
    parser = build_parser()

    args = parser.parse_args(["init", "site-name", "--template", "minimal"])

    assert args.command == "init"
    assert args.name == "site-name"
    assert args.template == "minimal"


def test_build_parser_accepts_serve_command() -> None:
    parser = build_parser()

    args = parser.parse_args(["serve", "--host", "0.0.0.0", "--port", "8000"])

    assert args.command == "serve"
    assert args.host == "0.0.0.0"
    assert args.port == 8000
