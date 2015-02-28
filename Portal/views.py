from django.shortcuts import render
from Portal.helpers.loop_requester import LoopSpider
from Portal.helpers.topic_filter import BaiduFilter
from Portal.helpers.zip_dir import zip_dir
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'Portal/index.html')


def loop(request):
    if request.method == 'GET':
        return render(request, 'Portal/loop_spider.html')
    elif request.method == 'POST':
        address = request.POST['address']
        spider = LoopSpider(address)
        record = spider.start()
        return render(request, 'Portal/loop_spider.html', {'address': address, 'result_list': record})


def loop_zip(request):
    address = request.GET['address']
    dir_name = 'download/' + address
    file_name = 'zip/' + address + '.zip'
    zip_dir(dir_name, file_name)
    file = open(file_name, 'rb').read()
    response = HttpResponse()
    response['Content-Disposition'] = 'attachment; filename=' + address + '.zip'
    response.write(file)
    return response


def baidu(request):
    if request.method == 'GET':
        return render(request, 'Portal/baidu_filter.html')
    elif request.method == 'POST':
        address = request.POST['address']
        baidu_filter = BaiduFilter(address)
        title, topics = baidu_filter.start()
        return render(request, 'Portal/baidu_filter.html', {'address': address, 'title': title, 'result_list': topics})
