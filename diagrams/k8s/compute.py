# This module is automatically generated by autogen.sh. DO NOT EDIT.

from . import _K8S

class _Compute(_K8S):
    _type = "compute"
    _icon_dir = "resources/k8s/compute"


class Cronjob(_Compute):
    _icon = "cronjob.png"
class Deploy(_Compute):
    _icon = "deploy.png"
class DS(_Compute):
    _icon = "ds.png"
class Job(_Compute):
    _icon = "job.png"
class Pod(_Compute):
    _icon = "pod.png"
class RS(_Compute):
    _icon = "rs.png"
class STS(_Compute):
    _icon = "sts.png"

# Aliases

Deployment = Deploy
DaemonSet = DS
ReplicaSet = RS
StatefulSet = STS