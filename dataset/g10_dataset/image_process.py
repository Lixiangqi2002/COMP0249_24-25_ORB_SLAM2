# import os
# import cv2

# input_dir = "rgb_old"
# output_dir = "rgb"
# os.makedirs(output_dir, exist_ok=True)

# image_files = sorted([f for f in os.listdir(input_dir) if f.endswith(('.png', '.jpg'))])

# # 5 FPS
# for idx, filename in enumerate(image_files):
#     if idx % 6 != 0:
#         continue  

#     img_path = os.path.join(input_dir, filename)
#     img = cv2.imread(img_path)

#     if img is None:
#         print(f"跳过无法读取的图像: {filename}")
#         continue

#     # Resize to 640x480
#     resized_img = cv2.resize(img, (640, 480))

#     # 保存新图像
#     out_path = os.path.join(output_dir, filename)
#     cv2.imwrite(out_path, resized_img)

# print("所有图像已处理完成，保存在:", output_dir)


import os

# === 配置区域 ===
image_folder = "rgb"
output_txt = "rgb.txt"
fps = 5  # 目标帧率
time_step = 1.0 / fps

# 获取图像文件并排序（按数字）
image_files = sorted(
    [f for f in os.listdir(image_folder) if f.endswith(('.png', '.jpg'))],
    key=lambda x: int(os.path.splitext(x)[0])
)

with open(output_txt, 'w') as f:
    for i, filename in enumerate(image_files):
        timestamp = i * time_step
        line = f"{timestamp:.6f} {image_folder}/{filename}\n"
        f.write(line)

print(f"✅ 已生成 {output_txt}，共写入 {len(image_files)} 行。")
