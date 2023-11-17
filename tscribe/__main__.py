import argparse
import logging
from pathlib import Path

import tscribe


def main():
    parser = argparse.ArgumentParser(
        description="Transform AWS Transcribe json files to docx, csv, sqlite and vtt."
    )
    parser.add_argument(
        "transcript",
        metavar="JSONPATH",
        type=str,
        help="Path to the AWS Transcribe json file.",
    )
    parser.add_argument(
        "-f",
        "--format",
        type=str,
        choices=["docx", "csv", "sqlite", "vtt"],
        default="docx",
        help="Output format. Default is docx.",
    )
    parser.add_argument(
        "-o",
        "--output_prefix",
        type=str,
        help="Output prefix minus the extension. Default is same as input file.",
    )
    parser.add_argument(
        "--verbose", "-v", help="Verbose logging.", action="store_true"
    )
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.INFO if args.verbose else logging.WARNING,
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    output_prefix = args.output_prefix or Path(args.transcript).with_suffix("")
    output_path = Path(output_prefix).with_suffix("." + args.format)
    tscribe.write(args.transcript, format=args.format, save_as=str(output_path))


if __name__ == "__main__":
    main()
