import pandas as pd


def csv_to_trc(csv_file_path, trc_file_path, data_rate=100, units="mm"):
    """
    Converts a CSV file containing 3D marker motion data into a TRC file.

    Parameters:
        csv_file_path (str): Path to the input CSV file.
        trc_file_path (str): Path to save the output TRC file.
        data_rate (int): Sampling rate (default is 100 Hz).
        units (str): Measurement units (default is "mm").
    """
    # Load CSV file
    df = pd.read_csv(csv_file_path)

    # Ensure 'Frame' column exists, or create it as sequential numbers
    if "Frame" not in df.columns:
        df.insert(0, "Frame", range(1, len(df) + 1))

    # Compute the 'Time' column based on frame number and sampling rate
    df["Time"] = df["Frame"] / data_rate

    # Extract marker names (remove _x, _y, _z for a clean list)
    marker_names = sorted(set([col.rstrip("xyz") for col in df.columns if col not in ["Frame", "Time"]]))

    # Define the number of markers
    num_markers = len(marker_names)
    num_frames = len(df)

    # Create TRC header
    header = [
        "PathFileType\t4\t(X/Y/Z)\t" + trc_file_path,
        "DataRate\tCameraRate\tNumFrames\tNumMarkers\tUnits\tOrigDataRate\tOrigDataStartFrame\tOrigNumFrames",
        f"{data_rate}\t{data_rate}\t{num_frames}\t{num_markers}\t{units}\t{data_rate}\t1\t{num_frames}",
        "Frame#\tTime\t" + "\t".join(marker_names),
        "\t\t" + "\t".join([str(i + 1) for i in range(num_markers)])  # Marker index row
    ]

    # Reorder columns for TRC format (Frame, Time, MarkerX1, MarkerY1, MarkerZ1, ...)
    trc_columns = ["Frame", "Time"] + [col for col in df.columns if col not in ["Frame", "Time"]]
    df_trc = df[trc_columns]

    # Write to TRC file
    with open(trc_file_path, "w") as trc_file:
        trc_file.write("\n".join(header) + "\n")  # Write header
        df_trc.to_csv(trc_file, sep="\t", index=False, header=False)  # Write data

    print(f"TRC file saved: {trc_file_path}")


# Example Usage
csv_file = "mediapipe_body_3d_xyz.csv"  # Replace with actual CSV file path
trc_file = "mediapipe_body_3d_xyz_output_data.trc"  # Output TRC file path
csv_to_trc(csv_file, trc_file,data_rate=60)
