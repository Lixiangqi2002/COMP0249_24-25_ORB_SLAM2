import numpy as np
from scipy.spatial.transform import Rotation as R

def parse_images_txt(images_txt_path):
    poses = []
    with open(images_txt_path, 'r') as f:
        lines = f.readlines()
        i = 0
        while i < len(lines):
            line = lines[i]
            if line.startswith("#") or line.strip() == "":
                i += 1
                continue
            parts = line.strip().split()
            if len(parts) >= 9 and parts[-1].endswith((".png", ".jpg", ".jpeg")):
                qw, qx, qy, qz = map(float, parts[1:5])
                tx, ty, tz = map(float, parts[5:8])

                r_cw = R.from_quat([qx, qy, qz, qw])
                t_cw = np.array([tx, ty, tz])

                r_wc = r_cw.inv()
                t_wc = -r_wc.apply(t_cw)

                qx2, qy2, qz2, qw2 = r_wc.as_quat()
                poses.append((t_wc[0], t_wc[1], t_wc[2], qx2, qy2, qz2, qw2))
                i += 2  # skip point observations line
            else:
                i += 1  # move to next line

    return poses


def read_timestamps(timestamps_txt_path):
    with open(timestamps_txt_path, 'r') as f:
        return [line.strip().split()[0] for line in f if line.strip()]

def write_results(timestamps, poses, output_path):
    with open(output_path, 'w') as f:
        for timestamp, pose in zip(timestamps, poses):
            print(f"Timestamp: {timestamp}, Pose: {pose}")
            tx, ty, tz, qx, qy, qz, qw = pose
            f.write(f"{timestamp} {tx:.6f} {ty:.6f} {tz:.6f} {qx:.6f} {qy:.6f} {qz:.6f} {qw:.6f}\n")

# ==== 路径配置 ====
timestamps_path = "outdoor/outdoor_results.txt"
images_txt_path = "outdoor/images.txt"
output_path = "outdoor/outdoor_colmap_results.txt"

# ==== 主流程 ====
timestamps = read_timestamps(timestamps_path)
poses = parse_images_txt(images_txt_path)

if len(timestamps) != len(poses):
    print(f"⚠️ Warning: Timestamps ({len(timestamps)}) and poses ({len(poses)}) count mismatch!")

write_results(timestamps, poses, output_path)
print(f"Written {len(poses)} entries to {output_path}")
