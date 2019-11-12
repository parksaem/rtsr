python main.py --upscale_factor 2 --batchSize 8 --testBatchSize 100 --nEpochs 20 --lr 0.001 --lr_dec 0.85 --cuda --sr_run 1

for i in 2 3 4 5 6 7 8
do
    mkdir "./dataset/DIV2K_train_HR/images/train_crop_sr/$i"

    mkdir "./dataset/DIV2K_train_HR/images/valid_sr/$i"

    for file in ./dataset/DIV2K_train_HR/images/valid_sr/1/*
    do
        name=${file##*/}
        python super_resolve.py --input_image "$file" --model model_epoch_20.pth --cuda --output_filename "./dataset/DIV2K_train_HR/images/valid_sr/$i/$name"
    done

    mkdir "./dataset/DIV2K_train_HR/images/valid_sr/crop_4x2/$i"

    for file in ./dataset/DIV2K_train_HR/images/valid_sr/crop_4x2/*
    do
        name=${file##*/}
        python super_resolve.py --input_image "$file" --model model_epoch_20.pth --cuda --output_filename "./dataset/DIV2K_train_HR/images/valid_sr/crop_4x2/$i/$name"
    done

    for file in ./dataset/DIV2K_train_HR/images/train_crop_sr/1/*
    do
        name=${file##*/}
        end0=${file##*9.png}
        end1=${file##*9.png}
        end2=${file##*9.png}
        end3=${file##*9.png}
        end4=${file##*9.png}
        if [ -z $end0 ] || [ -z $end1 ] || [ -z $end2 ] || [ -z $end3 ] || [ -z $end4 ]; then
            python super_resolve.py --input_image "$file" --model model_epoch_20.pth --cuda --output_filename "./dataset/DIV2K_train_HR/images/train_crop_sr/$i/$name"
        else
            python super_resolve.py --input_image "$file" --model model_epoch_20.pth --cuda --output_filename "./dataset/DIV2K_train_HR/images/train_crop_sr/$i/$name" &
        fi
    done

    mkdir train_weight_sr$i
    cp ./*.pth ./train_weight_sr$i

    python main.py --upscale_factor 2 --batchSize 8 --testBatchSize 100 --nEpochs 20 --lr 0.001 --lr_dec 0.85 --cuda --sr_run $i
done
