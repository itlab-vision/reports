##Результаты сегментации val датасета для обученной мною модели (largeFOV) после crf:

Percentage of pixels correctly labelled overall: 93.760%

###Accuracy for each class (pixel accuracy)
      background: 96.298%
       aeroplane: 94.828%
         bicycle: 86.105%
            bird: 91.340%
            boat: 88.158%
          bottle: 87.873%
             bus: 91.940%
             car: 90.064%
             cat: 96.585%
           chair: 62.706%
             cow: 88.468%
     diningtable: 65.416%
             dog: 91.196%
           horse: 90.512%
       motorbike: 93.403%
          person: 90.209%
     pottedplant: 79.171%
           sheep: 88.299%
            sofa: 59.030%
           train: 88.956%
       tvmonitor: 80.779%
-------------------------
Mean Class Accuracy: 85.778%

###Accuracy for each class (intersection/union measure)
      background: 93.168%
       aeroplane: 85.908%
         bicycle: 35.281%
            bird: 87.322%
            boat: 69.722%
          bottle: 74.262%
             bus: 87.573%
             car: 82.952%
             cat: 86.548%
           chair: 45.222%
             cow: 79.658%
     diningtable: 59.474%
             dog: 82.678%
           horse: 80.665%
       motorbike: 79.027%
          person: 81.400%
     pottedplant: 59.845%
           sheep: 82.783%
            sofa: 52.021%
           train: 81.957%
       tvmonitor: 65.882%
-------------------------
Average accuracy: 73.969%


##Результаты deeplab_largeFOV после crf на val:

Percentage of pixels correctly labelled overall: 94.681%

###Accuracy for each class (pixel accuracy)
      background: 96.193%
       aeroplane: 96.125%
         bicycle: 84.208%
            bird: 95.926%
            boat: 92.543%
          bottle: 91.124%
             bus: 96.722%
             car: 92.808%
             cat: 97.002%
           chair: 58.362%
             cow: 92.975%
     diningtable: 73.571%
             dog: 95.105%
           horse: 92.623%
       motorbike: 92.906%
          person: 92.018%
     pottedplant: 81.402%
           sheep: 95.133%
            sofa: 77.264%
           train: 95.157%
       tvmonitor: 86.179%
-------------------------
Mean Class Accuracy: 89.302%

###Accuracy for each class (intersection/union measure)
      background: 93.977%
       aeroplane: 87.282%
         bicycle: 38.160%
            bird: 88.285%
            boat: 73.817%
          bottle: 78.853%
             bus: 90.984%
             car: 84.549%
             cat: 89.581%
           chair: 42.027%
             cow: 87.134%
     diningtable: 65.741%
             dog: 87.891%
           horse: 83.470%
       motorbike: 80.470%
          person: 83.793%
     pottedplant: 65.909%
           sheep: 89.536%
            sofa: 65.953%
           train: 86.193%
       tvmonitor: 66.179%
-------------------------
Average accuracy: 77.609%

На тестовых данных их результаты падают на 7% как видно из [таблицы](http://host.robots.ox.ac.uk:8080/leaderboard/displaylb.php?cls=mean&challengeid=11&compid=6&submid=4581).


##Результаты deeplab_MSc_CRF_largeFOV на val:

Percentage of pixels correctly labelled overall: 95.310%

###Accuracy for each class (pixel accuracy)
      background: 96.864%
       aeroplane: 96.076%
         bicycle: 71.719%
            bird: 96.262%
            boat: 92.184%
          bottle: 91.954%
             bus: 97.317%
             car: 92.386%
             cat: 97.341%
           chair: 56.756%
             cow: 94.070%
     diningtable: 76.997%
             dog: 95.041%
           horse: 93.067%
       motorbike: 93.415%
          person: 92.707%
     pottedplant: 81.300%
           sheep: 95.854%
            sofa: 81.503%
           train: 95.287%
       tvmonitor: 87.170%
-------------------------
Mean Class Accuracy: 90.298%

###Accuracy for each class (intersection/union measure)
      background: 94.797%
       aeroplane: 89.681%
         bicycle: 61.726%
            bird: 89.355%
            boat: 79.238%
          bottle: 79.276%
             bus: 90.856%
             car: 85.748%
             cat: 89.883%
           chair: 43.446%
             cow: 88.147%
     diningtable: 65.292%
             dog: 89.012%
           horse: 84.817%
       motorbike: 81.897%
          person: 85.012%
     pottedplant: 68.625%
           sheep: 90.930%
            sofa: 66.651%
           train: 86.722%
       tvmonitor: 66.367%
-------------------------
Average accuracy: 80.350%
