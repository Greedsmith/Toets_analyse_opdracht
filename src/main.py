import argparse

# Defaults
DEFAULT_OUTPUT_FILE = None
DEFAULT_IMAGE_FILE = "visual.png"
DEFAULT_POINTS_FILE = "points.json"
DEFAULT_FMT = "pipe"
DEFAULT_EXPRESSION = "current_points / total_point * 9 + 1"

# Parse arguments
def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Analysis tool for data processing"
    )
    
    parser.add_argument(
        "input_file",
        type=str,
        help="Path to the input file"
    )
    
    parser.add_argument(
        "-o", "--output_file",
        type=str,
        default=DEFAULT_OUTPUT_FILE,
        help=f"Path to write the dataset (default: {DEFAULT_OUTPUT_FILE})"
    )

    parser.add_argument(
        "i", "--image_file",
        type=str,
        help=f"Output visual file name (defailt: {DEFAULT_IMAGE_FILE})"
    )

    parser.add_argument(
        "p", "--points_file",
        type=str,
        help=f"Config file containing the points per question (default: {DEFAULT_POINTS_FILE})"
    )

    parser.add_argument(
        "-f", "--fmt",
        type=str,
        choices=["grid", "html", "latex", "pipe", "psql"],
        default=DEFAULT_FMT,
        help=f"Format for tables (default: {DEFAULT_FMT})"
    )

    parser.add_argument(
        "-e", "expression",
        type=str,
        help=f"expression to calc grade (default: {DEFAULT_EXPRESSION})"
    )
    
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()
    print(f"Input file: {args.input_file}")
    print(f"Output file: {args.output_file}")
    print(f"Image file: {args.image_file}")
    print(f"Points file: {args.points_file}")
    print(f"Format: {args.fmt}")
    print(f"Expression: {args.expression}")
    