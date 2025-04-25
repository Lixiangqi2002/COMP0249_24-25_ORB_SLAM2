### 1. 这是一个什么任务的代码？

从以上内容推测，这段代码的任务是 **视觉 SLAM（Simultaneous Localization and Mapping，即同时定位与建图）**，它主要用于：

1. 相机/机器人定位（Localization）
   - 估算相机在三维空间中的运动轨迹（Pose Estimation）。
   - 适用于机器人导航、增强现实（AR）、自动驾驶等应用。
2. 环境建图（Mapping）
   - 在估算相机轨迹的同时，也可以构建环境的 3D 结构（例如点云地图）。
   - 适用于自动驾驶（街道建图）、机器人探索未知环境等。

**关键点**：

- 代码是 ORB-SLAM2，一个 **基于特征点（ORB Feature）的 SLAM 系统**。
- 适用于 **单目、立体、RGB-D 相机** 的 SLAM 任务。
- 使用 TUM 数据集（室内环境）和 KITTI 数据集（自动驾驶场景）进行 SLAM 测试。
- 运行时会估算相机的运动轨迹，并可以存储在 `.txt` 结果文件中。

**总结**： 这个代码的核心任务是 **视觉 SLAM（同时定位与建图）**，用于研究机器人、自动驾驶等领域的视觉定位问题。它的运行会读取视频/图像数据，提取特征点，进行位姿估计，并输出相机轨迹。

---



## 介绍 TUM 和 KITTI 数据集

### **TUM 数据集（RGB-D Dataset）**

- **全称**：Technical University of Munich RGB-D Dataset
- 数据内容：
  - 该数据集的不同子集（如 `fr1/xyz`）代表不同的拍摄环境，如办公桌周围、走廊等。
  - 包含 RGB（彩色）图像、深度图（Depth images）、相机轨迹（ground truth poses）。
  - 适用于 **RGB-D SLAM**（即利用 RGB 相机+深度信息进行 SLAM）。-
- `mono_tum TUM${fr_code}.yaml ${your_tum_dataset_folder} ${result_file_name}`
- `mono_tum TUM1.yaml dataset/TUM/rgbd_dataset_freiburg1_xyz results/fr01_results.txt`

### **KITTI 数据集**

采集自德国 Karlsruhe 城市街道，包含灰度图（monocular grey-scale images）、立体图（stereo images）、激光雷达（LiDAR）数据、GPS 信息等。

##### 数据内容：

- 包含 22 个不同的行驶序列（sequence），前 11 个提供了地面真实轨迹（ground truth）。

##### 指令详解：

- `mono_kitti KITTI${kitti_yaml_code}.yaml ${your_kitti_dataset_folder}/sequences/${kitti_sequence} ${result_file_name}`

- 这是一条运行 ORB-SLAM2 在 **KITTI 灰度图像数据集（Monocular 模式）** 上的命令。

- | 参数                                                       | 含义                                                   |
  | ---------------------------------------------------------- | ------------------------------------------------------ |
  | `mono_kitti`                                               | 执行的可执行程序，表示用“单目”模型运行 KITTI 数据集    |
  | `KITTI${kitti_yaml_code}.yaml`                             | 相机内参的配置文件（ORB-SLAM 已内置）                  |
  | `${your_kitti_dataset_folder}/sequences/${kitti_sequence}` | 你下载的 KITTI 数据集序列文件夹                        |
  | `${result_file_name}`                                      | 保存输出轨迹的结果文件名（例如 `kitti05_results.txt`） |



##### 举个例子——你要跑 KITTI 的第05号序列，那么：

- `kitti_sequence = 05`
- `kitti_yaml_code = 04-12`（因为 05 属于 04~12 范围）
- 你的数据路径假设是 `dataset/KITTY`
- 输出文件名是 `kitti05_results.txt`
- `mono_kitti KITTI04-12.yaml dataset/KITTY/sequences/05 results/kitti05_results.txt`

------

### 2. 你对 C++ 毫无了解，不知道 executables 如何运行以及会发生什么

从文档来看，ORB-SLAM2 编译后会生成多个可执行文件（executables），用于不同数据集和传感器类型。例如：

- `mono_tum` 用于 TUM 数据集（单目 SLAM）。
- `mono_kitti` 用于 KITTI 数据集（单目 SLAM）。
- `stereo_kitti` 用于 KITTI 数据集（立体 SLAM）。
- `rgbd_tum` 用于 TUM 数据集（RGB-D SLAM）。

#### **可执行文件的运行方式**

运行一个可执行文件的格式通常是：

```
./可执行文件 配置文件 数据集路径 结果文件
```

例如：

```
mono_tum TUM1.yaml rgbd_dataset_freiburg1_xyz fr01_results.txt
```

**这个命令在做什么？**

1. `mono_tum`：执行 ORB-SLAM2 的单目（monocular）SLAM 程序，针对 TUM 数据集。
2. `TUM1.yaml`：提供相机的参数配置文件，例如焦距、畸变参数等。
3. `rgbd_dataset_freiburg1_xyz`：数据集文件夹，程序会读取这里的图片数据。
4. `fr01_results.txt`：最终 SLAM 运行的结果会被保存到这个文件，包括相机的估计轨迹（pose 估计）。

#### **运行时会发生什么？**

1. **ORB-SLAM2 读取数据集**，加载图像并进行特征提取。
2. **SLAM 进行定位和建图**，通过视觉 SLAM 算法估算相机在环境中的位置，并可能重建环境地图。
3. **运行 GUI 界面**，程序通常会弹出一个窗口，显示 ORB-SLAM2 运行过程中的关键帧、轨迹等信息。
4. **保存运行结果**，比如相机的运动轨迹（pose 估计）等。

如果运行的是 KITTI 数据集：

```
mono_kitti KITTI04-12.yaml /sequences/05 results/kitti05_results.txt
```

它会：

1. 读取 `sequences/05` 目录下的 KITTI 数据，进行单目 SLAM 计算。
2. 估算相机轨迹并保存到 `kitti05_results.txt`。
3. 可能显示 GUI 界面，查看相机轨迹的可视化结果。

------

### 3. 数据集命名

```bash
dataset/
- KITTI/   # KITTI Dataset
- TUM/ # TUM Dataset
```



## EVO 

- 是一个用于 SLAM Evaluation 的工具包
- 支持 TUM trajectory files, KITTI pose files, ROS and ROS2 bagfile



#### EVO 常用子命令

| 命令          | 功能                                                |
| ------------- | --------------------------------------------------- |
| `evo_traj`    | 可视化或处理单个轨迹（支持 TUM、KITTI、euroc 格式） |
| `evo_ape`     | 计算绝对轨迹误差（Absolute Pose Error）             |
| `evo_rpe`     | 计算相对轨迹误差（Relative Pose Error）             |
| `evo_res`     | 显示多个评估结果的摘要（合并 `ape/rpe`）            |
| `evo_fig`     | 交互式可视化                                        |
| `evo_config`  | 设置和查看默认参数                                  |
| `evo_package` | 把结果导出为 zip 包，用于重现实验                   |



#### 比较常用的指令

- `evo_traj tum your_result.txt --plot`

- `evo_ape tum groundtruth.txt your_result.txt --plot`

- `evo_rpe tum groundtruth.txt your_result.txt --delta 1 --plot`

- ```bash
  # KITTI 07
  # 1. convert from kitti to tum
  python3 Evaluation/kitti_to_tum.py dataset/KITTY/sequences/07/07.txt dataset/KITTY/sequences/07/times.txt dataset/KITTY/sequences/07/07_tum.txt
  
  # 2. evo evaluation
  evo_ape tum  dataset/KITTY/sequences/07/07_tum.txt results/kitti07_results.txt -as --plot --plot_mode xz 
  
  # KITTI 10
  # 1. convert from kitti to tum
  python3 Evaluation/kitti_to_tum.py dataset/KITTY/sequences/10/10.txt dataset/KITTY/sequences/10/times.txt dataset/KITTY/sequences/10/10_tum.txt
  
  # 2. evo evaluation
  evo_ape tum  dataset/KITTY/sequences/10/10_tum.txt results/kitti10_results.txt -as --plot --plot_mode xz
  ```

- In  `Terminal 2`





#### 举个例子

- evo_ape tum gt.txt esimate.txt -as --plot --plot_mode xz****
  -   ref_file              reference trajectory file
      est_file              estimated trajectory file
  - 

## mono tum 输出分析

### System Initialization and Camera Param Loading

```yaml
Input sensor was set to: Monocular
Loading ORB Vocabulary...
Camera Parameters:
  fx, fy, cx, cy, k1, k2, k3, p1, p2
ORB Extractor Parameters:
  Number of Features, Scale Levels, etc.
```



---
## Part 1

#### 

#### Outlier Rejection

##### KITTI 07

- [Terminal2] mono_kitti KITTI04-12.yaml dataset/KITTY/sequences/07 results/outlier_reject/kitti/kitti07_results_outlier_reject.txt 

- mono_kitti KITTI04-12.yaml dataset/KITTY/sequences/07 results/feature/kitti/kitti07_results_4000.txt
- mono_kitti KITTI04-12.yaml dataset/KITTY/sequences/07 results/feature/kitti/kitti07_results_6000.txt
  
- [Terminal1] python3 Evaluation/kitti_to_tum.py dataset/KITTY/sequences/07/07.txt dataset/KITTY/sequences/07/times.txt dataset/KITTY/sequences/07/07_tum.txt

**APE**
[Terminal1] evo_ape tum dataset/KITTY/sequences/07/07_tum.txt results/kitti07_results_outlier_reject/kitti07_results_outlier_reject.txt -as --plot --plot_mode xz --save_plot results/outlier_reject/kitti/kitti07_results_outlier_reject_ape.png

       max      26.477420
      mean      8.865746
    median      8.047971
       min      0.814885
      rmse      9.808672
       sse      59938.860604
       std      4.196259

**evo_traj**
evo_traj tum results/kitti07_results_outlier_reject/kitti07_results_outlier_reject.txt \
         --ref dataset/KITTY/sequences/07/07_tum.txt \
         -as --plot --plot_mode xz \
         --save_plot results/outlier_reject/kitti/kitti07_results_outlier_reject_traj.png


**evo_rpe**
[Terminal1] evo_rpe tum dataset/KITTY/sequences/07/07_tum.txt results/kitti07_results_outlier_reject/kitti07_results_outlier_reject.txt -as --plot --plot_mode xz --save_plot results/kitti07_results_outlier_reject/kitti07_results_outlier_reject_rpe.png

RPE w.r.t. translation part (m)
for delta = 1 (frames) using consecutive pairs
(with Sim(3) Umeyama alignment)

       max      43.860468
      mean      0.236685
    median      0.123660
       min      0.003376
      rmse      1.773461
       sse      1956.292339
       std      1.757596



**TUM**

mono_tum TUM1.yaml dataset/TUM/rgbd_dataset_freiburg1_xyz fr1_xyz.txt
mono_tum TUM3.yaml dataset/TUM/rgbd_dataset_freiburg3_long_office_household results/raw/tum/fr3_results.txt

mono_tum TUM3.yaml dataset/TUM/rgbd_dataset_freiburg3_long_office_household results/feature/tum/fr3_results_1000.txt
mono_tum TUM3.yaml dataset/TUM/rgbd_dataset_freiburg3_long_office_household results/feature/tum/fr3_results_3000.txt
mono_tum TUM3.yaml dataset/TUM/rgbd_dataset_freiburg3_long_office_household results/feature/tum/fr3_results_5000.txt




## Part 2
mkdir -p myDataset/images/001 
mkdir -p myDataset/images/002 
mkdir -p myDataset/images/003 

ffmpeg -i myDataset/video/A001_04171723_C003.mov -q:v 1 myDataset/001/images/%06d.png
ffmpeg -i myDataset/video/A001_04171726_C004.mov -q:v 1 myDataset/002/images/%06d.png
ffmpeg -i myDataset/video/A001_04171730_C005.mov -q:v 1 myDataset/003/images/%06d.png


1000, 3000, 5000
2000, 4, 6


1. 整体建模图
2. KITTI
   1. 截图
   2. 视频1：Feature 匹配（绿点）
3. TUM
   1. 视频1：关注点云
   2. 视频2：Feature 匹配

mono_tum TUM3_5000.yaml dataset/TUM/rgbd_dataset_freiburg3_long_office_household results/feature/tum/fr3_results_5000.txt

mono_kitti KITTI04-12.yaml dataset/KITTY/sequences/07 results/feature/kitti/kitti07_results_2000.txt
mono_kitti KITTI04-12_4000.yaml dataset/KITTY/sequences/07 results/feature/kitti/kitti07_results_4000.txt
mono_kitti KITTI04-12_6000.yaml dataset/KITTY/sequences/07 results/feature/kitti/kitti07_results_6000.txt


mono_tum TUM3.yaml dataset/TUM/rgbd_dataset_freiburg3_long_office_household results/outlier_reject/tum/fr3_results_outlier_reject.txt
mono_kitti KITTI04-12.yaml dataset/KITTY/sequences/07 results/outlier_reject/kitti/kitti07_results_outlier_reject.txt

mono_tum TUM3.yaml dataset/TUM/rgbd_dataset_freiburg3_long_office_household results/loop_closure/tum/fr3_results_loop_closure.txt
mono_kitti KITTI04-12.yaml dataset/KITTY/sequences/07 results/loop_closure/kitti/kitti07_results_loop_closure.txt

KITTI_loop_closure_map_detail


mono_tum TUM1.yaml dataset/TUM/rgbd_dataset_freiburg1_xyz fr1_xyz.txt

mono_tum G10_indoor.yaml myDataset/004 results/G10/indoor/indoor_results.txt
ffmpeg -i myDataset/video/indoor_001.mp4 -vf fps=5 -q:v 1 myDataset/indoor_001/rgb/%06d.png
ffmpeg -i myDataset/video/indoor_001.mp4 -vf fps=10 -q:v 1 myDataset/indoor_001_fps10/rgb/%06d.png
ffmpeg -i myDataset/video/indoor_001.mp4 -vf fps=30 -q:v 1 myDataset/indoor_001_fps30/rgb/%06d.png

ffmpeg -i myDataset/video/indoor_002.mp4 -vf fps=10 -q:v 1 myDataset/indoor_002/rgb/%06d.png
ffmpeg -i myDataset/video/indoor_002.mp4 -vf fps=30 -q:v 1 myDataset/indoor_002_fps30/rgb/%06d.png

ffmpeg -i myDataset/video/indoor_003.mp4 -vf fps=30 -q:v 1 myDataset/indoor_003_fps30/rgb/%06d.png


mono_tum G10_indoor_2.yaml myDataset/indoor_001 results/G10/indoor/indoor_001_results.txt
mono_tum G10_indoor_2.yaml myDataset/indoor_001_fps10 results/G10/indoor/indoor_001_results_fps10.txt
mono_tum G10_indoor_2.yaml myDataset/indoor_001_fps30 results/G10/indoor/indoor_001_results_fps30.txt

mono_tum G10_indoor_2.yaml myDataset/indoor_002 results/G10/indoor/indoor_002_results.txt
mono_tum G10_indoor_2.yaml myDataset/indoor_002_fps30 results/G10/indoor/indoor_002_results_fps30.txt

mono_tum G10_indoor_2.yaml myDataset/indoor_003_fps30 results/G10/indoor/indoor_003_results_fps30.txt


mono_tum G10_indoor.yaml myDataset/004 results/G10/indoor/indoor_004.txt

ffmpeg -i myDataset/video/indoor_optimal.mp4 -vf fps=30 -q:v 1 myDataset/indoor_optimal/rgb/%06d.png
mono_tum G10_indoor.yaml myDataset/indoor_optimal results/G10/indoor/indoor_optimal.txt

