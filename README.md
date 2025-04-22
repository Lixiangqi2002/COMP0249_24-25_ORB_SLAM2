# Part 1

# TUM 
## TUM Original
Estimation
```
(navigation0249) selina-xiangqi@selina-xiangqi-Legion-R9000P-ARX8:~/ucl2024/robotVision_Navigation/COMP0249_24-25_ORB_SLAM2/dataset$ mono_tum TUM3.yaml rgbd_dataset_freiburg3_long_office_household/ fr03_results.txt

ORB-SLAM2 Copyright (C) 2014-2016 Raul Mur-Artal, University of Zaragoza.
(modifications carried out at UCL, 2022)
This program comes with ABSOLUTELY NO WARRANTY;
This is free software, and you are welcome to redistribute it
under certain conditions. See LICENSE.txt.

Input sensor was set to: Monocular

Loading ORB Vocabulary. This could take a while...
Using the binary cache file
Vocabulary loaded in 0.09s

Camera Parameters: 
- fx: 535.4
- fy: 539.2
- cx: 320.1
- cy: 247.6
- k1: 0
- k2: 0
- p1: 0
- p2: 0
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
Images in the sequence: 2585

New Map created with 158 points
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
System Shutdown
-------

median tracking time: 0.0109459
mean tracking time: 0.0117162

Saving camera trajectory to fr03_results.txt ...

trajectory saved!
All done

```
APE
```
(navigation0249) selina-xiangqi@selina-xiangqi-Legion-R9000P-ARX8:~/ucl2024/robotVision_Navigation/COMP0249_24-25_ORB_SLAM2/dataset$ evo_ape tum rgbd_dataset_freiburg3_long_office_household/groundtruth.txt fr03_results.txt -as --plot --plot_mode xz --save_plot tum_fr03_ape.png
APE w.r.t. translation part (m)
(with Sim(3) Umeyama alignment)

       max	0.036452
      mean	0.011115
    median	0.009880
       min	0.000367
      rmse	0.012481
       sse	0.398503
       std	0.005679

```
RPE
```
(navigation0249) selina-xiangqi@selina-xiangqi-Legion-R9000P-ARX8:~/ucl2024/robotVision_Navigation/COMP0249_24-25_ORB_SLAM2/dataset$ evo_rpe tum rgbd_dataset_freiburg3_long_office_household/groundtruth.txt fr03_results.txt -as --plot --plot_mode xz --save_plot tum_fr03_rpe.png
RPE w.r.t. translation part (m)
for delta = 1 (frames) using consecutive pairs
(with Sim(3) Umeyama alignment)

       max	0.028161
      mean	0.004716
    median	0.003922
       min	0.000275
      rmse	0.005637
       sse	0.081258
       std	0.003089
```

## TUM Features
### 3000
Estimation
```
(navigation0249) selina-xiangqi@selina-xiangqi-Legion-R9000P-ARX8:~/ucl2024/robotVision_Navigation/COMP0249_24-25_ORB_SLAM2/dataset$ mono_tum TUM3.yaml rgbd_dataset_freiburg3_long_office_household/ fr03_results_3000.txt

ORB-SLAM2 Copyright (C) 2014-2016 Raul Mur-Artal, University of Zaragoza.
(modifications carried out at UCL, 2022)
This program comes with ABSOLUTELY NO WARRANTY;
This is free software, and you are welcome to redistribute it
under certain conditions. See LICENSE.txt.

Input sensor was set to: Monocular

Loading ORB Vocabulary. This could take a while...
Using the binary cache file
Vocabulary loaded in 0.10s

Camera Parameters: 
- fx: 535.4
- fy: 539.2
- cx: 320.1
- cy: 247.6
- k1: 0
- k2: 0
- p1: 0
- p2: 0
- fps: 30
- color order: RGB (ignored if grayscale)

ORB Extractor Parameters: 
- Number of Features: 3000
- Scale Levels: 8
- Scale Factor: 1.2
- Initial Fast Threshold: 20
- Minimum Fast Threshold: 7

-------
Start processing sequence ...
Images in the sequence: 2585

New Map created with 582 points
Loop detected!
Local Mapping STOP
Local Mapping RELEASE
Starting Global Bundle Adjustment
Global Bundle Adjustment finished
Updating map ...
Local Mapping STOP
Local Mapping RELEASE
Map updated!
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
System Shutdown
-------

median tracking time: 0.0223829
mean tracking time: 0.0242436

Saving camera trajectory to fr03_results_3000.txt ...

trajectory saved!
All done

```
APE
```
(navigation0249) selina-xiangqi@selina-xiangqi-Legion-R9000P-ARX8:~/ucl2024/robotVision_Navigation/COMP0249_24-25_ORB_SLAM2/dataset$ evo_ape tum rgbd_dataset_freiburg3_long_office_household/groundtruth.txt fr03_results_3000.txt -as --plot --plot_mode xz --save_plot tum_fr03_ape_3000.png
APE w.r.t. translation part (m)
(with Sim(3) Umeyama alignment)

       max	0.429761
      mean	0.123313
    median	0.096019
       min	0.002105
      rmse	0.151247
       sse	58.424123
       std	0.087575

```
RPE
```
(navigation0249) selina-xiangqi@selina-xiangqi-Legion-R9000P-ARX8:~/ucl2024/robotVision_Navigation/COMP0249_24-25_ORB_SLAM2/dataset$ evo_rpe tum rgbd_dataset_freiburg3_long_office_household/groundtruth.txt fr03_results_3000.txt -as --plot --plot_mode xz --save_plot tum_fr03_rpe_3000.png
RPE w.r.t. translation part (m)
for delta = 1 (frames) using consecutive pairs
(with Sim(3) Umeyama alignment)

       max	0.285454
      mean	0.010592
    median	0.005579
       min	0.000234
      rmse	0.024743
       sse	1.563032
       std	0.022362

```

### 5000 
Estimation
```
(navigation0249) selina-xiangqi@selina-xiangqi-Legion-R9000P-ARX8:~/ucl2024/robotVision_Navigation/COMP0249_24-25_ORB_SLAM2/dataset$ mono_tum TUM3.yaml rgbd_dataset_freiburg3_long_office_household/ fr03_results_5000.txt

ORB-SLAM2 Copyright (C) 2014-2016 Raul Mur-Artal, University of Zaragoza.
(modifications carried out at UCL, 2022)
This program comes with ABSOLUTELY NO WARRANTY;
This is free software, and you are welcome to redistribute it
under certain conditions. See LICENSE.txt.

Input sensor was set to: Monocular

Loading ORB Vocabulary. This could take a while...
Using the binary cache file
Vocabulary loaded in 0.10s

Camera Parameters: 
- fx: 535.4
- fy: 539.2
- cx: 320.1
- cy: 247.6
- k1: 0
- k2: 0
- p1: 0
- p2: 0
- fps: 30
- color order: RGB (ignored if grayscale)

ORB Extractor Parameters: 
- Number of Features: 5000
- Scale Levels: 8
- Scale Factor: 1.2
- Initial Fast Threshold: 20
- Minimum Fast Threshold: 7

-------
Start processing sequence ...
Images in the sequence: 2585

New Map created with 462 points
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
System Shutdown
-------

median tracking time: 0.02805
mean tracking time: 0.0303095

Saving camera trajectory to fr03_results_5000.txt ...

trajectory saved!
All done

```
APE
```
(navigation0249) selina-xiangqi@selina-xiangqi-Legion-R9000P-ARX8:~/ucl2024/robotVision_Navigation/COMP0249_24-25_ORB_SLAM2/dataset$ evo_ape tum rgbd_dataset_freiburg3_long_office_household/groundtruth.txt fr03_results_5000.txt -as --plot --plot_mode xz --save_plot tum_fr03_ape_5000.png
APE w.r.t. translation part (m)
(with Sim(3) Umeyama alignment)

       max	0.697844
      mean	0.148727
    median	0.108102
       min	0.014591
      rmse	0.189153
       sse	91.343775
       std	0.116873

```
RPE
```
(navigation0249) selina-xiangqi@selina-xiangqi-Legion-R9000P-ARX8:~/ucl2024/robotVision_Navigation/COMP0249_24-25_ORB_SLAM2/dataset$ evo_rpe tum rgbd_dataset_freiburg3_long_office_household/groundtruth.txt fr03_results_5000.txt -as --plot --plot_mode xz --save_plot tum_fr03_rpe_5000.png
RPE w.r.t. translation part (m)
for delta = 1 (frames) using consecutive pairs
(with Sim(3) Umeyama alignment)

       max	0.718423
      mean	0.022506
    median	0.007155
       min	0.000283
      rmse	0.061519
       sse	9.658215
       std	0.057254

```

### Compare 1000, 3000, 5000 with GT
```
(navigation0249) selina-xiangqi@selina-xiangqi-Legion-R9000P-ARX8:~/ucl2024/robotVision_Navigation/COMP0249_24-25_ORB_SLAM2/dataset$ evo_traj tum fr03_results.txt fr03_results_3000.txt fr03_results_5000.txt --ref=rgbd_dataset_freiburg3_long_office_household/groundtruth.txt -va --plot --plot_mode xz -as --save_plot tum_fr03_compare_features.png 
--------------------------------------------------------------------------------
Loaded 2558 stamps and poses from: fr03_results.txt
Loaded 2554 stamps and poses from: fr03_results_3000.txt
Loaded 2553 stamps and poses from: fr03_results_5000.txt
Loaded 8710 stamps and poses from: rgbd_dataset_freiburg3_long_office_household/groundtruth.txt
--------------------------------------------------------------------------------
Found 2558 of max. 2558 possible matching timestamps between...
	reference
and:	fr03_results.txt
..with max. time diff.: 0.01 (s) and time offset: 0.0 (s).
--------------------------------------------------------------------------------
Aligning fr03_results.txt to reference.
Aligning using Umeyama's method... (with scale correction)
Rotation of alignment:
[[-0.99958363 -0.01194273 -0.02626679]
 [ 0.01725461  0.4822243  -0.87587785]
 [ 0.02312686 -0.87596638 -0.48181745]]
Translation of alignment:
[-0.69439828  2.69913405  1.74473895]
Scale correction: 2.5382504118349623
--------------------------------------------------------------------------------
Found 2554 of max. 2554 possible matching timestamps between...
	reference
and:	fr03_results_3000.txt
..with max. time diff.: 0.01 (s) and time offset: 0.0 (s).
--------------------------------------------------------------------------------
Aligning fr03_results_3000.txt to reference.
Aligning using Umeyama's method... (with scale correction)
Rotation of alignment:
[[-0.99608279 -0.00570882 -0.08824109]
 [ 0.07511853  0.47183934 -0.87847871]
 [ 0.0466507  -0.88166606 -0.46956221]]
Translation of alignment:
[-0.6304575   2.80503989  1.75305908]
Scale correction: 2.5170061152045564
--------------------------------------------------------------------------------
Found 2553 of max. 2553 possible matching timestamps between...
	reference
and:	fr03_results_5000.txt
..with max. time diff.: 0.01 (s) and time offset: 0.0 (s).
--------------------------------------------------------------------------------
Aligning fr03_results_5000.txt to reference.
Aligning using Umeyama's method... (with scale correction)
Rotation of alignment:
[[-9.98566738e-01 -8.75051189e-04 -5.35135850e-02]
 [ 4.67972816e-02  4.70907725e-01 -8.80940366e-01]
 [ 2.59708285e-02 -8.82182038e-01 -4.70191841e-01]]
Translation of alignment:
[-0.71391032  2.76026874  1.73161206]
Scale correction: 2.3675001996563374
--------------------------------------------------------------------------------
name:	fr03_results
infos:
	duration (s)	86.2361330986023
	nr. of poses	2558
	path length (m)	25.34406127097212
	pos_end (m)	[-0.56838691  1.98046128  1.54239906]
	pos_start (m)	[-0.61760596  2.71804483  1.74639093]
	t_end (s)	1341848067.862808
	t_start (s)	1341847981.626675
--------------------------------------------------------------------------------
name:	fr03_results_3000
infos:
	duration (s)	86.10396194458008
	nr. of poses	2554
	path length (m)	39.300094168370144
	pos_end (m)	[-0.59813392  2.04237435  1.54243564]
	pos_start (m)	[-0.59933441  2.82673215  1.74508837]
	t_end (s)	1341848067.862808
	t_start (s)	1341847981.758846
--------------------------------------------------------------------------------
name:	fr03_results_5000
infos:
	duration (s)	86.06814908981323
	nr. of poses	2553
	path length (m)	68.44186596896168
	pos_end (m)	[-0.61795442  2.01186862  1.56137419]
	pos_start (m)	[-0.62112158  2.7942142   1.7366584 ]
	t_end (s)	1341848067.862808
	t_start (s)	1341847981.794659
--------------------------------------------------------------------------------
name:	groundtruth
infos:
	duration (s)	87.08949995040894
	nr. of poses	8710
	path length (m)	22.19745284585122
	pos_end (m)	[-0.5503  1.9752  1.5438]
	pos_start (m)	[-0.6832  2.6909  1.7373]
	t_end (s)	1341848067.8795
	t_start (s)	1341847980.79
--------------------------------------------------------------------------------

```


## TUM No Outlier Rejection 
Estimation
```
(navigation0249) selina-xiangqi@selina-xiangqi-Legion-R9000P-ARX8:~/ucl2024/robotVision_Navigation/COMP0249_24-25_ORB_SLAM2/dataset$ mono_tum TUM3.yaml rgbd_dataset_freiburg3_long_office_household/ fr03_results_no_outlier_rejection.txt

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
- fx: 535.4
- fy: 539.2
- cx: 320.1
- cy: 247.6
- k1: 0
- k2: 0
- p1: 0
- p2: 0
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
Images in the sequence: 2585

New Map created with 163 points
Viewer thread finished.
Viewer started, waiting for thread.
System Shutdown
-------

median tracking time: 0.00939642
mean tracking time: 0.00946798

Saving camera trajectory to fr03_results_no_outlier_rejection.txt ...

trajectory saved!
All done

```

APE
```
(navigation0249) selina-xiangqi@selina-xiangqi-Legion-R9000P-ARX8:~/ucl2024/robotVision_Navigation/COMP0249_24-25_ORB_SLAM2/dataset$ evo_ape tum rgbd_dataset_freiburg3_long_office_household/groundtruth.txt fr03_results_no_outlier_rejection.txt -as --plot --plot_mode xz --save_plot tum_fr03_no_outlier_rejection_ape.png
APE w.r.t. translation part (m)
(with Sim(3) Umeyama alignment)

       max	1.511066
      mean	0.218821
    median	0.137154
       min	0.010786
      rmse	0.325207
       sse	208.240193
       std	0.240576

```

RPE
```
(navigation0249) selina-xiangqi@selina-xiangqi-Legion-R9000P-ARX8:~/ucl2024/robotVision_Navigation/COMP0249_24-25_ORB_SLAM2/dataset$ evo_rpe tum rgbd_dataset_freiburg3_long_office_household/groundtruth.txt fr03_results_no_outlier_rejection.txt -as --plot --plot_mode xz --save_plot tum_fr03_no_outlier_rejection_rpe.png
RPE w.r.t. translation part (m)
for delta = 1 (frames) using consecutive pairs
(with Sim(3) Umeyama alignment)

       max	2.419446
      mean	0.012400
    median	0.009169
       min	0.000430
      rmse	0.056455
       sse	6.272268
       std	0.055076

```

Compare
```
(navigation0249) selina-xiangqi@selina-xiangqi-Legion-R9000P-ARX8:~/ucl2024/robotVision_Navigation/COMP0249_24-25_ORB_SLAM2/dataset$ evo_traj tum fr03_results.txt fr03_results_no_outlier_rejection.txt --ref=rgbd_dataset_freiburg3_long_office_household/groundtruth.txt -va --plot --plot_mode xz -as --save_plot tum_fr03_compare_no_oyutlier_rejection.png 
--------------------------------------------------------------------------------
Loaded 2558 stamps and poses from: fr03_results.txt
Loaded 1969 stamps and poses from: fr03_results_no_outlier_rejection.txt
Loaded 8710 stamps and poses from: rgbd_dataset_freiburg3_long_office_household/groundtruth.txt
--------------------------------------------------------------------------------
Found 2558 of max. 2558 possible matching timestamps between...
	reference
and:	fr03_results.txt
..with max. time diff.: 0.01 (s) and time offset: 0.0 (s).
--------------------------------------------------------------------------------
Aligning fr03_results.txt to reference.
Aligning using Umeyama's method... (with scale correction)
Rotation of alignment:
[[-0.99958363 -0.01194273 -0.02626679]
 [ 0.01725461  0.4822243  -0.87587785]
 [ 0.02312686 -0.87596638 -0.48181745]]
Translation of alignment:
[-0.69439828  2.69913405  1.74473895]
Scale correction: 2.5382504118349623
--------------------------------------------------------------------------------
Found 1969 of max. 1969 possible matching timestamps between...
	reference
and:	fr03_results_no_outlier_rejection.txt
..with max. time diff.: 0.01 (s) and time offset: 0.0 (s).
--------------------------------------------------------------------------------
Aligning fr03_results_no_outlier_rejection.txt to reference.
Aligning using Umeyama's method... (with scale correction)
Rotation of alignment:
[[-0.99319494  0.1139805  -0.02392207]
 [ 0.07875429  0.50596825 -0.85894929]
 [-0.08579966 -0.85498805 -0.51150156]]
Translation of alignment:
[-0.68264439  2.79808644  1.66585198]
Scale correction: 2.4965329119950246
--------------------------------------------------------------------------------
name:	fr03_results
infos:
	duration (s)	86.2361330986023
	nr. of poses	2558
	path length (m)	25.34406127097212
	pos_end (m)	[-0.56838691  1.98046128  1.54239906]
	pos_start (m)	[-0.61760596  2.71804483  1.74639093]
	t_end (s)	1341848067.862808
	t_start (s)	1341847981.626675
--------------------------------------------------------------------------------
name:	fr03_results_no_outlier_rejection
infos:
	duration (s)	86.20407009124756
	nr. of poses	1969
	path length (m)	30.999722807728432
	pos_end (m)	[-0.56735581  2.05836247  1.45628079]
	pos_start (m)	[-0.60032461  2.81874834  1.67826612]
	t_end (s)	1341848067.862808
	t_start (s)	1341847981.658738
--------------------------------------------------------------------------------
name:	groundtruth
infos:
	duration (s)	87.08949995040894
	nr. of poses	8710
	path length (m)	22.19745284585122
	pos_end (m)	[-0.5503  1.9752  1.5438]
	pos_start (m)	[-0.6832  2.6909  1.7373]
	t_end (s)	1341848067.8795
	t_start (s)	1341847980.79
--------------------------------------------------------------------------------

```

## TUM LOOP NO CLOSURE
Estimation
```
(navigation0249) selina-xiangqi@selina-xiangqi-Legion-R9000P-ARX8:~/ucl2024/robotVision_Navigation/COMP0249_24-25_ORB_SLAM2/dataset$ mono_tum TUM3.yaml rgbd_dataset_freiburg3_long_office_household/ fr03_results_no_loop_closure.txt

ORB-SLAM2 Copyright (C) 2014-2016 Raul Mur-Artal, University of Zaragoza.
(modifications carried out at UCL, 2022)
This program comes with ABSOLUTELY NO WARRANTY;
This is free software, and you are welcome to redistribute it
under certain conditions. See LICENSE.txt.

Input sensor was set to: Monocular

Loading ORB Vocabulary. This could take a while...
Using the binary cache file
Vocabulary loaded in 0.09s

Camera Parameters: 
- fx: 535.4
- fy: 539.2
- cx: 320.1
- cy: 247.6
- k1: 0
- k2: 0
- p1: 0
- p2: 0
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
Images in the sequence: 2585

New Map created with 163 points
Viewer thread finished.
Viewer started, waiting for thread.
System Shutdown
-------

median tracking time: 0.0112035
mean tracking time: 0.0116479

Saving camera trajectory to fr03_results_no_loop_closure.txt ...

trajectory saved!
All done

```

APE
```
(navigation0249) selina-xiangqi@selina-xiangqi-Legion-R9000P-ARX8:~/ucl2024/robotVision_Navigation/COMP0249_24-25_ORB_SLAM2/dataset$ evo_ape tum rgbd_dataset_freiburg3_long_office_household/groundtruth.txt fr03_results_no_loop_closure.txt -as --plot --plot_mode xz --save_plot tum_fr03_no_loop_ape.png
APE w.r.t. translation part (m)
(with Sim(3) Umeyama alignment)

       max	0.069766
      mean	0.021849
    median	0.018926
       min	0.001330
      rmse	0.025250
       sse	1.630248
       std	0.012657

```

RPE
```
(navigation0249) selina-xiangqi@selina-xiangqi-Legion-R9000P-ARX8:~/ucl2024/robotVision_Navigation/COMP0249_24-25_ORB_SLAM2/dataset$ evo_rpe tum rgbd_dataset_freiburg3_long_office_household/groundtruth.txt fr03_results_no_loop_closure.txt -as --plot --plot_mode xz --save_plot tum_fr03_no_loop_rpe.png
RPE w.r.t. translation part (m)
for delta = 1 (frames) using consecutive pairs
(with Sim(3) Umeyama alignment)

       max	0.027567
      mean	0.004534
    median	0.003850
       min	0.000195
      rmse	0.005371
       sse	0.073733
       std	0.002880

```

Trajectory Comparison
```
(navigation0249) selina-xiangqi@selina-xiangqi-Legion-R9000P-ARX8:~/ucl2024/robotVision_Navigation/COMP0249_24-25_ORB_SLAM2/dataset$ evo_traj tum fr03_results.txt fr03_results_no_loop_closure.txt --ref=rgbd_dataset_freiburg3_long_office_household/groundtruth.txt -va --plot --plot_mode xz -as --save_plot tum_fr03_compare_no_loop.png 
--------------------------------------------------------------------------------
Loaded 2558 stamps and poses from: fr03_results.txt
Loaded 2557 stamps and poses from: fr03_results_no_loop_closure.txt
Loaded 8710 stamps and poses from: rgbd_dataset_freiburg3_long_office_household/groundtruth.txt
--------------------------------------------------------------------------------
Found 2558 of max. 2558 possible matching timestamps between...
	reference
and:	fr03_results.txt
..with max. time diff.: 0.01 (s) and time offset: 0.0 (s).
--------------------------------------------------------------------------------
Aligning fr03_results.txt to reference.
Aligning using Umeyama's method... (with scale correction)
Rotation of alignment:
[[-0.99958363 -0.01194273 -0.02626679]
 [ 0.01725461  0.4822243  -0.87587785]
 [ 0.02312686 -0.87596638 -0.48181745]]
Translation of alignment:
[-0.69439828  2.69913405  1.74473895]
Scale correction: 2.5382504118349623
--------------------------------------------------------------------------------
Found 2557 of max. 2557 possible matching timestamps between...
	reference
and:	fr03_results_no_loop_closure.txt
..with max. time diff.: 0.01 (s) and time offset: 0.0 (s).
--------------------------------------------------------------------------------
Aligning fr03_results_no_loop_closure.txt to reference.
Aligning using Umeyama's method... (with scale correction)
Rotation of alignment:
[[-0.99940819 -0.01248926 -0.03205132]
 [ 0.021996    0.48434523 -0.87460041]
 [ 0.02644702 -0.87478781 -0.48378387]]
Translation of alignment:
[-0.65856223  2.6420813   1.73773886]
Scale correction: 2.4142894718975114
--------------------------------------------------------------------------------
name:	fr03_results
infos:
	duration (s)	86.2361330986023
	nr. of poses	2558
	path length (m)	25.34406127097212
	pos_end (m)	[-0.56838691  1.98046128  1.54239906]
	pos_start (m)	[-0.61760596  2.71804483  1.74639093]
	t_end (s)	1341848067.862808
	t_start (s)	1341847981.626675
--------------------------------------------------------------------------------
name:	fr03_results_no_loop_closure
infos:
	duration (s)	86.20407009124756
	nr. of poses	2557
	path length (m)	24.915821462224464
	pos_end (m)	[-0.57088958  1.99791653  1.54386649]
	pos_start (m)	[-0.57901367  2.66631864  1.73708248]
	t_end (s)	1341848067.862808
	t_start (s)	1341847981.658738
--------------------------------------------------------------------------------
name:	groundtruth
infos:
	duration (s)	87.08949995040894
	nr. of poses	8710
	path length (m)	22.19745284585122
	pos_end (m)	[-0.5503  1.9752  1.5438]
	pos_start (m)	[-0.6832  2.6909  1.7373]
	t_end (s)	1341848067.8795
	t_start (s)	1341847980.79
--------------------------------------------------------------------------------

```




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

## KITTI No Outlier Rejection 
Estimation
```
(navigation0249) selina-xiangqi@selina-xiangqi-Legion-R9000P-ARX8:~/ucl2024/robotVision_Navigation/COMP0249_24-25_ORB_SLAM2/dataset$ mono_kitti KITTI04-12.yaml 07 kitti07_results_no_outlier_rejection.txt 

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

New Map created with 159 points
Viewer thread finished.
Viewer started, waiting for thread.
Tracking thread joined...
-------

median tracking time: 0.0167509
mean tracking time: 0.0167295

Saving camera trajectory to kitti07_results_no_outlier_rejection.txt ...

trajectory saved!

```
APE
```
(navigation0249) selina-xiangqi@selina-xiangqi-Legion-R9000P-ARX8:~/ucl2024/robotVision_Navigation/COMP0249_24-25_ORB_SLAM2/dataset$ evo_ape tum 07/07_tum.txt kitti07_results_no_outlier_rejection.txt -as --plot --plot_mode xz --save_plot kitty07_no_outlier_rejection_ape.png
APE w.r.t. translation part (m)
(with Sim(3) Umeyama alignment)

       max	25.559268
      mean	8.590777
    median	8.016600
       min	0.784415
      rmse	9.572419
       sse	58918.867519
       std	4.222530

```

RPE
```
(navigation0249) selina-xiangqi@selina-xiangqi-Legion-R9000P-ARX8:~/ucl2024/robotVision_Navigation/COMP0249_24-25_ORB_SLAM2/dataset$ evo_rpe tum 07/07_tum.txt kitti07_results_no_outlier_rejection.txt -as --plot --plot_mode xz --save_plot kitty07_no_outlier_rejection_rpe.png
RPE w.r.t. translation part (m)
for delta = 1 (frames) using consecutive pairs
(with Sim(3) Umeyama alignment)

       max	43.377455
      mean	0.204594
    median	0.109147
       min	0.004394
      rmse	1.720274
       sse	1899.898889
       std	1.708065

```

Compare
```
(navigation0249) selina-xiangqi@selina-xiangqi-Legion-R9000P-ARX8:~/ucl2024/robotVision_Navigation/COMP0249_24-25_ORB_SLAM2/dataset$ evo_traj tum kitti07_results.txt kitti07_results_no_outlier_rejection.txt --ref=07/07_tum.txt -va --plot --plot_mode xz -as --save_plot kitti07_compare_no_oyutlier_rejection.png 
--------------------------------------------------------------------------------
Loaded 1096 stamps and poses from: kitti07_results.txt
Loaded 643 stamps and poses from: kitti07_results_no_outlier_rejection.txt
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
Found 643 of max. 643 possible matching timestamps between...
	reference
and:	kitti07_results_no_outlier_rejection.txt
..with max. time diff.: 0.01 (s) and time offset: 0.0 (s).
--------------------------------------------------------------------------------
Aligning kitti07_results_no_outlier_rejection.txt to reference.
Aligning using Umeyama's method... (with scale correction)
Rotation of alignment:
[[ 0.99738257 -0.01195194  0.07131029]
 [ 0.01130369  0.9998911   0.00948734]
 [-0.07141592 -0.00865643  0.99740906]]
Translation of alignment:
[-10.62791836   0.09139192   4.93330085]
Scale correction: 9.320975595635101
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
name:	kitti07_results_no_outlier_rejection
infos:
	duration (s)	113.810101
	nr. of poses	643
	path length (m)	599.6728700909739
	pos_end (m)	[-11.30782465   0.01465784  11.75671582]
	pos_start (m)	[-10.64373259   0.0909995    5.2968149 ]
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


# Part 2

## Outdoor

### ORB SLAM 2
Estimation
```
(navigation0249) selina-xiangqi@selina-xiangqi-Legion-R9000P-ARX8:~/ucl2024/robotVision_Navigation/COMP0249_24-25_ORB_SLAM2/dataset/g10_dataset$ mono_tum  G10Outdoor.yaml outdoor outdoor_results.txt

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
- fx: 768
- fy: 768
- cx: 320
- cy: 240
- k1: 0
- k2: 0
- p1: 0
- p2: 0
- fps: 5
- color order: RGB (ignored if grayscale)

ORB Extractor Parameters: 
- Number of Features: 2000
- Scale Levels: 8
- Scale Factor: 1.2
- Initial Fast Threshold: 20
- Minimum Fast Threshold: 7

-------
Start processing sequence ...
Images in the sequence: 904

New Map created with 166 points
Local Mapping STOP
Local Mapping RELEASE
Viewer thread finished.
Viewer started, waiting for thread.
System Shutdown
-------

median tracking time: 0.0260453
mean tracking time: 0.0269453

Saving camera trajectory to outdoor_results.txt ...

trajectory saved!
All done


```

APE
```
(navigation0249) selina-xiangqi@selina-xiangqi-Legion-R9000P-ARX8:~/ucl2024/robotVision_Navigation/COMP0249_24-25_ORB_SLAM2/dataset/g10_dataset$ evo_ape tum outdoor/outdoor_results.txt outdoor/outdoor_colmap_results.txt  -as --plot --plot_mode xz --save_plot outdoor_ape.png
APE w.r.t. translation part (m)
(with Sim(3) Umeyama alignment)

       max	0.242633
      mean	0.034259
    median	0.026323
       min	0.003368
      rmse	0.048379
       sse	2.106462
       std	0.034159

```

RPE
```
(navigation0249) selina-xiangqi@selina-xiangqi-Legion-R9000P-ARX8:~/ucl2024/robotVision_Navigation/COMP0249_24-25_ORB_SLAM2/dataset/g10_dataset$ evo_rpe tum outdoor/outdoor_results.txt outdoor/outdoor_colmap_results.txt  -as --plot --plot_mode xz --save_plot outdoor_rpe.png
RPE w.r.t. translation part (m)
for delta = 1 (frames) using consecutive pairs
(with Sim(3) Umeyama alignment)

       max	0.030098
      mean	0.003973
    median	0.003228
       min	0.000173
      rmse	0.005161
       sse	0.023950
       std	0.003295

```
Comparison with COLMAP
```
(navigation0249) selina-xiangqi@selina-xiangqi-Legion-R9000P-ARX8:~/ucl2024/robotVision_Navigation/COMP0249_24-25_ORB_SLAM2/dataset/g10_dataset$ evo_traj tum  outdoor/outdoor_results.txt --ref=outdoor/outdoor_colmap_results.txt -p --plot_mode xyz -as --save_plot outdoor_compare.png
--------------------------------------------------------------------------------
name:	outdoor_results
infos:	900 poses, 24.668m path length, 179.800s duration
--------------------------------------------------------------------------------
name:	outdoor_colmap_results
infos:	900 poses, 22.580m path length, 179.800s duration
--------------------------------------------------------------------------------
```

## Indoor
Estimation
