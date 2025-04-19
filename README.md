# Part 1

# TUM 
## TUM Original
Estimation
```
(navigation0249) selina-xiangqi@selina-xiangqi-Legion-R9000P-ARX8:~/ucl2024/robotVision_Navigation/COMP0249_24-25_ORB_SLAM2/dataset$ mono_tum TUM2.yaml rgbd_dataset_freiburg2_large_with_loop fr02_results.txt

ORB-SLAM2 Copyright (C) 2014-2016 Raul Mur-Artal, University of Zaragoza.
(modifications carried out at UCL, 2022)
This program comes with ABSOLUTELY NO WARRANTY;
This is free software, and you are welcome to redistribute it
under certain conditions. See LICENSE.txt.

Input sensor was set to: Monocular

Loading ORB Vocabulary. This could take a while...
Using the text file. This could take a while...
Padded dictionary size = 1082074
Saving the binary cache to /home/selina-xiangqi/ucl2024/robotVision_Navigation/COMP0249_24-25_ORB_SLAM2/Install/var/lib/orbslam2/ORBvoc.bin
Vocabulary loaded in 3.08s

Camera Parameters: 
- fx: 520.909
- fy: 521.007
- cx: 325.141
- cy: 249.702
- k1: 0.231222
- k2: -0.784899
- k3: 0.917205
- p1: -0.003257
- p2: -0.000105
- fps: 30
- color order: RGB (ignored if grayscale)

ORB Extractor Parameters: 
- Number of Features: 1000
- Scale Levels: 8
- Scale Factor: 1.2
- Initial Fast Threshold: 20
- Minimum Fast Threshold: 7

-------
Start processing sequence ...
Images in the sequence: 5182

New Map created with 129 points
Viewer thread finished.
Viewer started, waiting for thread.
System Shutdown
-------

median tracking time: 0.00855813
mean tracking time: 0.0089992

Saving camera trajectory to fr02_results.txt ...

trajectory saved!
All done
```
APE
```
(navigation0249) selina-xiangqi@selina-xiangqi-Legion-R9000P-ARX8:~/ucl2024/robotVision_Navigation/COMP0249_24-25_ORB_SLAM2/dataset$ evo_ape tum rgbd_dataset_freiburg2_large_with_loop/groundtruth.txt fr02_results.txt -as --plot --plot_mode xz --save_plot tum_fr02_ape.png
APE w.r.t. translation part (m)
(with Sim(3) Umeyama alignment)

       max	0.282611
      mean	0.051659
    median	0.046365
       min	0.002891
      rmse	0.059501
       sse	2.938527
       std	0.029526
```
RPE
```
(navigation0249) selina-xiangqi@selina-xiangqi-Legion-R9000P-ARX8:~/ucl2024/robotVision_Navigation/COMP0249_24-25_ORB_SLAM2/dataset$ evo_rpe tum rgbd_dataset_freiburg2_large_with_loop/groundtruth.txt fr02_results.txt -as --plot --plot_mode xz --save_plot tum_fr02_rpe.png
RPE w.r.t. translation part (m)
for delta = 1 (frames) using consecutive pairs
(with Sim(3) Umeyama alignment)

       max	0.227649
      mean	0.016966
    median	0.010893
       min	0.000794
      rmse	0.028466
       sse	0.671727
       std	0.022857
```

## TUM Features

## TUM LOOP NO CLOSURE



# KITTI (07; to use sequence No.10, replace all 07 to 10)
## KITTI Original
GT TO TUM
```
(navigation0249) selina-xiangqi@selina-xiangqi-Legion-R9000P-ARX8:~/ucl2024/robotVision_Navigation/COMP0249_24-25_ORB_SLAM2/Evaluation$ python kitti_to_tum.py ~/ucl2024/robotVision_Navigation/COMP0249_24-25_ORB_SLAM2/dataset/07/07.txt ~/ucl2024/robotVision_Navigation/COMP0249_24-25_ORB_SLAM2/dataset/07/times.txt ~/ucl2024/robotVision_Navigation/COMP0249_24-25_ORB_SLAM2/dataset/07/07_tum.txt
```
Estimation
```
(navigation0249) selina-xiangqi@selina-xiangqi-Legion-R9000P-ARX8:~/ucl2024/robotVision_Navigation/COMP0249_24-25_ORB_SLAM2/dataset$ mono_kitti KITTI04-12.yaml 07 kitti07_results.txt

ORB-SLAM2 Copyright (C) 2014-2016 Raul Mur-Artal, University of Zaragoza.
(modifications carried out at UCL, 2022)
This program comes with ABSOLUTELY NO WARRANTY;
This is free software, and you are welcome to redistribute it
under certain conditions. See LICENSE.txt.

Input sensor was set to: Monocular

Loading ORB Vocabulary. This could take a while...
Using the binary cache file
Vocabulary loaded in 0.14s

Camera Parameters: 
- fx: 707.091
- fy: 707.091
- cx: 601.887
- cy: 183.11
- k1: 0
- k2: 0
- p1: 0
- p2: 0
- fps: 10
- color order: RGB (ignored if grayscale)

ORB Extractor Parameters: 
- Number of Features: 2000
- Scale Levels: 8
- Scale Factor: 1.2
- Initial Fast Threshold: 20
- Minimum Fast Threshold: 7

-------
Start processing sequence ...
Images in the sequence: 1101

New Map created with 165 points
Loop detected!
Local Mapping STOP
Local Mapping RELEASE
Starting Global Bundle Adjustment
Global Bundle Adjustment finished
Updating map ...
Local Mapping STOP
Local Mapping RELEASE
Map updated!
Viewer thread finished.
Viewer started, waiting for thread.
Tracking thread joined...
-------

median tracking time: 0.0138701
mean tracking time: 0.0146444

Saving camera trajectory to kitti07_results.txt ...

trajectory saved!
```
APE
```
(navigation0249) selina-xiangqi@selina-xiangqi-Legion-R9000P-ARX8:~/ucl2024/robotVision_Navigation/COMP0249_24-25_ORB_SLAM2/dataset$ evo_ape tum 07/07_tum.txt kitti07_results.txt -as --plot --plot_mode xz --save_plot kitty07_ape.png
APE w.r.t. translation part (m)
(with Sim(3) Umeyama alignment)

       max	8.383594
      mean	3.724264
    median	3.807131
       min	0.203045
      rmse	3.930284
       sse	16930.060939
       std	1.255785

```
RPE
```
(navigation0249) selina-xiangqi@selina-xiangqi-Legion-R9000P-ARX8:~/ucl2024/robotVision_Navigation/COMP0249_24-25_ORB_SLAM2/dataset$ evo_rpe tum kitti07_results.txt 07/07_tum.txt  -as --plot --plot_mode xz --save_plot kitty07_results_rpe.png
RPE w.r.t. translation part (m)
for delta = 1 (frames) using consecutive pairs
(with Sim(3) Umeyama alignment)

       max	0.183995
      mean	0.028323
    median	0.013929
       min	0.000097
      rmse	0.042342
       sse	1.963134
       std	0.031474

```

## KITTI 07 Feature
### 4000
Estimation
```
(navigation0249) selina-xiangqi@selina-xiangqi-Legion-R9000P-ARX8:~/ucl2024/robotVision_Navigation/COMP0249_24-25_ORB_SLAM2/dataset$ mono_kitti KITTI04-12.yaml 07 kitti07_results_feature_4000.txt

ORB-SLAM2 Copyright (C) 2014-2016 Raul Mur-Artal, University of Zaragoza.
(modifications carried out at UCL, 2022)
This program comes with ABSOLUTELY NO WARRANTY;
This is free software, and you are welcome to redistribute it
under certain conditions. See LICENSE.txt.

Input sensor was set to: Monocular

Loading ORB Vocabulary. This could take a while...
Using the binary cache file
Vocabulary loaded in 0.14s

Camera Parameters: 
- fx: 707.091
- fy: 707.091
- cx: 601.887
- cy: 183.11
- k1: 0
- k2: 0
- p1: 0
- p2: 0
- fps: 10
- color order: RGB (ignored if grayscale)

ORB Extractor Parameters: 
- Number of Features: 4000
- Scale Levels: 8
- Scale Factor: 1.2
- Initial Fast Threshold: 20
- Minimum Fast Threshold: 7

-------
Start processing sequence ...
Images in the sequence: 1101

New Map created with 382 points
Loop detected!
Local Mapping STOP
Local Mapping RELEASE
Starting Global Bundle Adjustment
Global Bundle Adjustment finished
Updating map ...
Local Mapping STOP
Local Mapping RELEASE
Map updated!
Viewer thread finished.
Viewer started, waiting for thread.
Tracking thread joined...
-------

median tracking time: 0.0192454
mean tracking time: 0.0203938

Saving camera trajectory to kitti07_results_feature_4000.txt ...

trajectory saved!

```
APE
```
(navigation0249) selina-xiangqi@selina-xiangqi-Legion-R9000P-ARX8:~/ucl2024/robotVision_Navigation/COMP0249_24-25_ORB_SLAM2/dataset$ evo_ape tum 07/07_tum.txt kitti07_results_feature_4000.txt -as --plot --plot_mode xz
APE w.r.t. translation part (m)
(with Sim(3) Umeyama alignment)

       max	6.233862
      mean	2.884539
    median	2.846273
       min	0.395835
      rmse	3.025714
       sse	10042.975118
       std	0.913444

```
RPE
```
(navigation0249) selina-xiangqi@selina-xiangqi-Legion-R9000P-ARX8:~/ucl2024/robotVision_Navigation/COMP0249_24-25_ORB_SLAM2/dataset$ evo_rpe tum  07/07_tum.txt  kitti07_results_feature_4000.txt  -as --plot --plot_mode xz --save_plot kitty07_feature_4000_rpe.png
RPE w.r.t. translation part (m)
for delta = 1 (frames) using consecutive pairs
(with Sim(3) Umeyama alignment)

       max	2.164023
      mean	0.419492
    median	0.285860
       min	0.000744
      rmse	0.585692
       sse	375.966324
       std	0.408731


```

### 6000
Estimation
```
(navigation0249) selina-xiangqi@selina-xiangqi-Legion-R9000P-ARX8:~/ucl2024/robotVision_Navigation/COMP0249_24-25_ORB_SLAM2/dataset$ mono_kitti KITTI04-12.yaml 07 kitti07_results_feature_6000.txt

ORB-SLAM2 Copyright (C) 2014-2016 Raul Mur-Artal, University of Zaragoza.
(modifications carried out at UCL, 2022)
This program comes with ABSOLUTELY NO WARRANTY;
This is free software, and you are welcome to redistribute it
under certain conditions. See LICENSE.txt.

Input sensor was set to: Monocular

Loading ORB Vocabulary. This could take a while...
Using the binary cache file
Vocabulary loaded in 0.14s

Camera Parameters: 
- fx: 707.091
- fy: 707.091
- cx: 601.887
- cy: 183.11
- k1: 0
- k2: 0
- p1: 0
- p2: 0
- fps: 10
- color order: RGB (ignored if grayscale)

ORB Extractor Parameters: 
- Number of Features: 6000
- Scale Levels: 8
- Scale Factor: 1.2
- Initial Fast Threshold: 20
- Minimum Fast Threshold: 7

-------
Start processing sequence ...
Images in the sequence: 1101

New Map created with 607 points
Loop detected!
Local Mapping STOP
Local Mapping RELEASE
Starting Global Bundle Adjustment
Global Bundle Adjustment finished
Updating map ...
Local Mapping STOP
Local Mapping RELEASE
Map updated!
Viewer thread finished.
Viewer started, waiting for thread.
Tracking thread joined...
-------

median tracking time: 0.0233534
mean tracking time: 0.0251394

Saving camera trajectory to kitti07_results_feature_6000.txt ...

trajectory saved!

```

APE
```
(navigation0249) selina-xiangqi@selina-xiangqi-Legion-R9000P-ARX8:~/ucl2024/robotVision_Navigation/COMP0249_24-25_ORB_SLAM2/dataset$ evo_ape tum 07/07_tum.txt kitti07_results_feature_6000.txt -as --plot --plot_mode xz
APE w.r.t. translation part (m)
(with Sim(3) Umeyama alignment)

       max	8.789715
      mean	2.988044
    median	2.877393
       min	0.205106
      rmse	3.149707
       sse	10882.959167
       std	0.996118


```

RPE
```
(navigation0249) selina-xiangqi@selina-xiangqi-Legion-R9000P-ARX8:~/ucl2024/robotVision_Navigation/COMP0249_24-25_ORB_SLAM2/dataset$ evo_rpe tum  07/07_tum.txt  kitti07_results_feature_6000.txt  -as --plot --plot_mode xz --save_plot kitty07_feature_6000_rpe.png
RPE w.r.t. translation part (m)
for delta = 1 (frames) using consecutive pairs
(with Sim(3) Umeyama alignment)

       max	4.993400
      mean	0.516838
    median	0.336618
       min	0.002348
      rmse	0.780630
       sse	667.884095
       std	0.585032
```

### Compare 2000, 4000, 6000 with GT
```
(navigation0249) selina-xiangqi@selina-xiangqi-Legion-R9000P-ARX8:~/ucl2024/robotVision_Navigation/COMP0249_24-25_ORB_SLAM2/dataset$ evo_traj tum kitti07_results.txt kitti07_results_feature_4000.txt kitti07_results_feature_6000.txt --ref=07/07_tum.txt -va --plot --plot_mode xz -as
--------------------------------------------------------------------------------
Loaded 1096 stamps and poses from: kitti07_results.txt
Loaded 1097 stamps and poses from: kitti07_results_feature_4000.txt
Loaded 1097 stamps and poses from: kitti07_results_feature_6000.txt
Loaded 1101 stamps and poses from: 07/07_tum.txt
--------------------------------------------------------------------------------
Found 1096 of max. 1096 possible matching timestamps between...
	reference
and:	kitti07_results.txt
..with max. time diff.: 0.01 (s) and time offset: 0.0 (s).
--------------------------------------------------------------------------------
Aligning kitti07_results.txt to reference.
Aligning using Umeyama's method... (with scale correction)
Rotation of alignment:
[[ 0.99899153  0.00410553  0.044711  ]
 [-0.00388186  0.99997952 -0.00508842]
 [-0.04473097  0.00490973  0.998987  ]]
Translation of alignment:
[-2.69692759  0.12189494 -2.7127717 ]
Scale correction: 10.762813754301684
--------------------------------------------------------------------------------
Found 1097 of max. 1097 possible matching timestamps between...
	reference
and:	kitti07_results_feature_4000.txt
..with max. time diff.: 0.01 (s) and time offset: 0.0 (s).
--------------------------------------------------------------------------------
Aligning kitti07_results_feature_4000.txt to reference.
Aligning using Umeyama's method... (with scale correction)
Rotation of alignment:
[[ 0.99955873  0.00230078  0.02961499]
 [-0.0021374   0.99998233 -0.00554729]
 [-0.02962723  0.00548155  0.99954599]]
Translation of alignment:
[-1.58702634  0.10975954 -3.21275395]
Scale correction: 11.77242602179473
--------------------------------------------------------------------------------
Found 1097 of max. 1097 possible matching timestamps between...
	reference
and:	kitti07_results_feature_6000.txt
..with max. time diff.: 0.01 (s) and time offset: 0.0 (s).
--------------------------------------------------------------------------------
Aligning kitti07_results_feature_6000.txt to reference.
Aligning using Umeyama's method... (with scale correction)
Rotation of alignment:
[[ 0.99970624 -0.00122686  0.02420577]
 [ 0.00126748  0.99999781 -0.00166271]
 [-0.02420368  0.00169291  0.99970561]]
Translation of alignment:
[-1.69659202  0.23490063 -3.40360758]
Scale correction: 9.65683399589673
--------------------------------------------------------------------------------
name:	kitti07_results
infos:
	duration (s)	113.810101
	nr. of poses	1096
	path length (m)	734.6429605073652
	pos_end (m)	[-3.8011658  -0.05963026  5.57862272]
	pos_start (m)	[-2.69548234  0.11655785 -2.28660938]
	t_end (s)	114.3296
	t_start (s)	0.519499
--------------------------------------------------------------------------------
name:	kitti07_results_feature_4000
infos:
	duration (s)	113.913978
	nr. of poses	1097
	path length (m)	804.015691815851
	pos_end (m)	[-2.89697646 -0.09249514  5.62246842]
	pos_start (m)	[-1.60589074  0.10222065 -2.8501778 ]
	t_end (s)	114.3296
	t_start (s)	0.415622
--------------------------------------------------------------------------------
name:	kitti07_results_feature_6000
infos:
	duration (s)	113.913978
	nr. of poses	1097
	path length (m)	947.3936546985004
	pos_end (m)	[-3.03987039  0.05444336  5.4937654 ]
	pos_start (m)	[-1.7182772   0.22856003 -3.03166681]
	t_end (s)	114.3296
	t_start (s)	0.415622
--------------------------------------------------------------------------------
name:	07_tum
infos:
	duration (s)	114.3296
	nr. of poses	1101
	path length (m)	694.6967407086909
	pos_end (m)	[-1.643555 -0.191078  9.367453]
	pos_start (m)	[5.551115e-17 0.000000e+00 2.220446e-16]
	t_end (s)	114.3296
	t_start (s)	0.0
```

## KITTI 07 LOOP NO CLOSURE
Estimation
```
(navigation0249) selina-xiangqi@selina-xiangqi-Legion-R9000P-ARX8:~/ucl2024/robotVision_Navigation/COMP0249_24-25_ORB_SLAM2/dataset$ mono_kitti KITTI04-12.yaml 07 kitti07_results_no_loop_closure.txt

ORB-SLAM2 Copyright (C) 2014-2016 Raul Mur-Artal, University of Zaragoza.
(modifications carried out at UCL, 2022)
This program comes with ABSOLUTELY NO WARRANTY;
This is free software, and you are welcome to redistribute it
under certain conditions. See LICENSE.txt.

Input sensor was set to: Monocular

Loading ORB Vocabulary. This could take a while...
Using the binary cache file
Vocabulary loaded in 0.13s

Camera Parameters: 
- fx: 707.091
- fy: 707.091
- cx: 601.887
- cy: 183.11
- k1: 0
- k2: 0
- p1: 0
- p2: 0
- fps: 10
- color order: RGB (ignored if grayscale)

ORB Extractor Parameters: 
- Number of Features: 2000
- Scale Levels: 8
- Scale Factor: 1.2
- Initial Fast Threshold: 20
- Minimum Fast Threshold: 7

-------
Start processing sequence ...
Images in the sequence: 1101

New Map created with 165 points
Viewer thread finished.
Viewer started, waiting for thread.
Tracking thread joined...
-------

median tracking time: 0.0136731
mean tracking time: 0.0141749

Saving camera trajectory to kitti07_results_no_loop_closure.txt ...

trajectory saved!

```

APE
```
(navigation0249) selina-xiangqi@selina-xiangqi-Legion-R9000P-ARX8:~/ucl2024/robotVision_Navigation/COMP0249_24-25_ORB_SLAM2/dataset$ evo_ape tum 07/07_tum.txt kitti07_results_no_loop_closure.txt -as --plot --plot_mode xz --save_plot kitty07_no_loop.png
APE w.r.t. translation part (m)
(with Sim(3) Umeyama alignment)

       max	47.472095
      mean	14.487352
    median	13.543359
       min	1.088121
      rmse	17.626794
       sse	340531.452702
       std	10.040942

```

RPE
```
(navigation0249) selina-xiangqi@selina-xiangqi-Legion-R9000P-ARX8:~/ucl2024/robotVision_Navigation/COMP0249_24-25_ORB_SLAM2/dataset$ evo_rpe tum 07/07_tum.txt kitti07_results_no_loop_closure.txt  -as --plot --plot_mode xz --save_plot kitty07_no_loop_rpe.png
RPE w.r.t. translation part (m)
for delta = 1 (frames) using consecutive pairs
(with Sim(3) Umeyama alignment)

       max	0.347094
      mean	0.120760
    median	0.104467
       min	0.001117
      rmse	0.150538
       sse	24.814517
       std	0.089882

```

Trajectory Comparison
```
(navigation0249) selina-xiangqi@selina-xiangqi-Legion-R9000P-ARX8:~/ucl2024/robotVision_Navigation/COMP0249_24-25_ORB_SLAM2/dataset$ evo_traj tum kitti07_results.txt kitti07_results_no_loop_closure.txt --ref=07/07_tum.txt -va --plot --plot_mode xz -as --save_plot kitty07_no_loop.png
--------------------------------------------------------------------------------
Loaded 1096 stamps and poses from: kitti07_results.txt
Loaded 1096 stamps and poses from: kitti07_results_no_loop_closure.txt
Loaded 1101 stamps and poses from: 07/07_tum.txt
--------------------------------------------------------------------------------
Found 1096 of max. 1096 possible matching timestamps between...
	reference
and:	kitti07_results.txt
..with max. time diff.: 0.01 (s) and time offset: 0.0 (s).
--------------------------------------------------------------------------------
Aligning kitti07_results.txt to reference.
Aligning using Umeyama's method... (with scale correction)
Rotation of alignment:
[[ 0.99899153  0.00410553  0.044711  ]
 [-0.00388186  0.99997952 -0.00508842]
 [-0.04473097  0.00490973  0.998987  ]]
Translation of alignment:
[-2.69692759  0.12189494 -2.7127717 ]
Scale correction: 10.762813754301684
--------------------------------------------------------------------------------
Found 1096 of max. 1096 possible matching timestamps between...
	reference
and:	kitti07_results_no_loop_closure.txt
..with max. time diff.: 0.01 (s) and time offset: 0.0 (s).
--------------------------------------------------------------------------------
Aligning kitti07_results_no_loop_closure.txt to reference.
Aligning using Umeyama's method... (with scale correction)
Rotation of alignment:
[[ 0.99227949 -0.01304314  0.12333402]
 [ 0.01360181  0.99990069 -0.00368882]
 [-0.12327366  0.00533791  0.99235836]]
Translation of alignment:
[-45.36468518   1.28221198  14.32948601]
Scale correction: 6.1612968760262765
--------------------------------------------------------------------------------
name:	kitti07_results
infos:
	duration (s)	113.810101
	nr. of poses	1096
	path length (m)	734.6429605073652
	pos_end (m)	[-3.8011658  -0.05963026  5.57862272]
	pos_start (m)	[-2.69548234  0.11655785 -2.28660938]
	t_end (s)	114.3296
	t_start (s)	0.519499
--------------------------------------------------------------------------------
name:	kitti07_results_no_loop_closure
infos:
	duration (s)	113.810101
	nr. of poses	1096
	path length (m)	627.4862821286998
	pos_end (m)	[16.91048077 -1.3748008  15.7684835 ]
	pos_start (m)	[-45.3605908    1.27965276  14.5807596 ]
	t_end (s)	114.3296
	t_start (s)	0.519499
--------------------------------------------------------------------------------
name:	07_tum
infos:
	duration (s)	114.3296
	nr. of poses	1101
	path length (m)	694.6967407086909
	pos_end (m)	[-1.643555 -0.191078  9.367453]
	pos_start (m)	[5.551115e-17 0.000000e+00 2.220446e-16]
	t_end (s)	114.3296
	t_start (s)	0.0
--------------------------------------------------------------------------------
```