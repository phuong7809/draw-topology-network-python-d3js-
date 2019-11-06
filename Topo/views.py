from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import schedule
import time

# Create your views here.
def index(request):
    return render(request, 'topo/index5.html')

def api_topo(request):
    data = {
    "links": [
        {
            "source": "usplnAGVPCLAB1003", 
            "target": "AR21-U23-ICB1",
            "type": "15"
        }, 
        {
            "source": "usplnAGVPCLAB1003", 
            "target": "AR21-U23-ICB2",
            "type": "30"
        }, 
        {
            "source": "usplnAGVPCLAB1004", 
            "target": "AR21-U23-ICB2",
            "type": "10"
        },
	    {
            "source": "usplnAGVPCLAB1003", 
            "target": "ABCD",
            "type": "50"
        },
        {
            "source": "AR21-U23-ICB1", 
            "target": "pln-ng1-esxm3",
            "type": "80"
        }, 
        {
            "source": "AR21-U23-ICB1", 
            "target": "pln-ng1-esxm4",
            "type": "50"
        }, 
        {
            "source": "AR21-U23-ICB2", 
            "target": "pln-ng1-esxm4",
            "type": "90"
        },
	    {
            "source": "AR21-U23-ICB2", 
            "target": "1111",
            "type": "40"
        }
    ], 
    "nodes": [
	    {
            "group": "1", 
            "id": "1111"
        },
        {
            "group": "1", 
            "id": "pln-ng1-esxm3"
        }, 
        {
            "group": "1", 
            "id": "pln-ng1-esxm4"
        }, 
        {
            "group": "3", 
            "id": "usplnAGVPCLAB1003"
        }, 
        {
            "group": "3", 
            "id": "usplnAGVPCLAB1004"
        }, 
        {
            "group": "2", 
            "id": "AR21-U23-ICB1"
        }, 
        {
            "group": "2", 
            "id": "AR21-U23-ICB2"
        },
	    {
            "group": "2", 
            "id": "ABCD"
        },
        {
            "group": "1", 
            "id": "AAAA"
        }
    ]
    }
    return JsonResponse(data)
 
# schedule.every(10).minutes.do(api_topo)
# while True:
#     schedule.run_pending()
#     time.sleep(1)


@csrf_exempt
def ajax_neighbor(request):
    if request.is_ajax():
        device = request.GET.get('device')
        if device == 'AR21-U23-ICB2':
            data =  {
            "data1": [
        {
            "local_intf": "Ten-GigabitEthernet1/0/17", 
            "neighbor": "AR21-U23-ICB2", 
            "neighbor_intf": "Ten-GigabitEthernet1/0/17",
        }, 
        {
            "local_intf": "Ten-GigabitEthernet1/0/18", 
            "neighbor": "AR21-U23-ICB2", 
            "neighbor_intf": "Ten-GigabitEthernet1/0/18",
        },
        {
            "local_intf": "TwentyGigE1/0/1", 
            "neighbor": "ng1-esx13", 
            "neighbor_intf": "0050-5696-2a40"
        }, 
            ]
             }
        elif device == '1111':
            data =  {
            "data1": [
        {
            "local_intf": "Ten-GigabitEthernet1/0/17", 
            "neighbor": "AR21-U23-ICB2", 
            "neighbor_intf": "Ten-GigabitEthernet1/0/17",
        }, 
        {
            "local_intf": "Ten-GigabitEthernet1/0/18", 
            "neighbor": "AR21-U23-ICB2", 
            "neighbor_intf": "Ten-GigabitEthernet1/0/18",
        },
            ]
             }
        else:
            data={
                'ok':'ok'
            }
    return JsonResponse(data)
