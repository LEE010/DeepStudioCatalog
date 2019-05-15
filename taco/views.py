from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Tacotron
# import urllib
import os
import sys
# import time
# Create your views here.
def tacotron_index(request):
    return render(request, 'tacotron_index.html')

def results(request):
    tacotrons = Tacotron.objects.order_by('-id')
    return render(request, 'tacotron_results.html', {'tacotrons': tacotrons})

def create(request):
    tacotron = Tacotron()
    tacotron.target = request.GET['target']
    tacotron.type = request.GET['type']
    tacotron.pub_date = timezone.datetime.now()

    print('*'*1000)
    # kss='tacotron_num_gpus=1,wavenet_num_gpus=1,tacotron_batch_size=32,tacotron_synthesis_batch_size=1,wavenet_batch_size=8,wavenet_synthesis_batch_size=20'
    # type에 따라 디렉토리를 다르게 만들어 구분하게 하는 코드 필요
    now = str(timezone.datetime.now()).split(' ')
    file_name = now[0] + '-' +now[1].split('.')[0].replace(':','-')
    wav_path = '/media/' + now[0] + '-' + file_name +'.wav'
    # wav_path = '/media/'+ type +'/' + now[0] + '-' + file_name +'.wav'
    text_path = './results/text/'+file_name+".txt"
    # print(now)
    # print(file_name)
    # return(render(request, 'tacotron_index.html'))
    with open(text_path, "w") as f:
        f.write(request.GET['target'])
 # --hparams="+kss
    os.system("python ../Tacotron-2/synthesize.py --model='Tacotron' --text_list='" +text_path+ "' --tacotron_name='"+ request.GET['type'] + "-Tacotron-2' --output_dir=./result/"+'--input_dir='+ request.GET['type']+'_training_data/')

    print('*'*20)
    tacotron.url= '/media/wav-0_' + file_name + '_0-mel.wav'
    tacotron.save()

    return redirect('/results')
