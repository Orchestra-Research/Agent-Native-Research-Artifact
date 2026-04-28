# Environment

## Software
- **Python**: Not specified in paper (paper is from 2015 — likely Python 2.7 era).
- **Framework**: Not specified in paper. The reference implementation [19] is Caffe (Jia et al., 2014); the paper does not commit to a specific framework. Modern reproductions typically use PyTorch ≥1.5 or TensorFlow ≥2.x.
- **Inference protocol libraries**: Standard Caffe data layers for color/scale augmentation; per-pixel mean subtraction.

## Hardware
- **CIFAR-10**: 2 GPUs (§4.2). GPU model not specified.
- **ImageNet**: GPU count not specified in §3.4. Mini-batch size 256 implies a multi-GPU setup; commonly 8 GPUs at the time.
- **Detection (Faster R-CNN, Appendix A)**: 8 GPUs; mini-batch 8 images per RPN step (1/GPU), 16 images per Fast R-CNN step.

## Key dependencies (inferred — not enumerated in paper)
- Standard CNN training stack of the era (Caffe + cuDNN 4/5).
- For modern reproduction: torch / torchvision / numpy.

## Random seeds
- Not specified in paper. The 110-layer CIFAR ResNet is reported as **5 runs with mean ± std** ("best (mean ± std)" in Table 6 caption: 6.43% best, 6.61 ± 0.16% mean ± std), so authors do average over seeds for that depth.

## Data
- **ImageNet 2012**: 1.28M train / 50k val / 100k test images (1000 classes).
- **CIFAR-10**: 50k train / 10k test images (10 classes), 32×32. 45k/5k train/val split used to determine the 64k iteration budget.
- **PASCAL VOC 2007 / 2012**: trainval splits "07+12" (5k+16k) or "07++12" (5k+16k+10k VOC07 trainval+test).
- **MS COCO**: 80k train + 40k val (Appendix B).

## Reproduction notes
- The paper does not release a code drop in the document itself; modern reference implementations live in `torchvision.models.resnet`.
- BN momentum, exact MSRA fan-mode, learning-rate decay's "plateau" trigger threshold are unspecified; reproductions typically use BN momentum 0.1 (PyTorch default) and a manual step schedule at iters {300k, 600k} or based on epoch count.
