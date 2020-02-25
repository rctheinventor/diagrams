# This module is automatically generated by autogen.sh. DO NOT EDIT.

from . import _AlibabaCloud

class _Compute(_AlibabaCloud):
    _type = "compute"
    _icon_dir = "resources/alibabacloud/compute"


class AutoScaling(_Compute):
    _icon = "auto-scaling.png"
class BatchCompute(_Compute):
    _icon = "batch-compute.png"
class ContainerRegistry(_Compute):
    _icon = "container-registry.png"
class ContainerService(_Compute):
    _icon = "container-service.png"
class ElasticComputeService(_Compute):
    _icon = "elastic-compute-service.png"
class ElasticContainerInstance(_Compute):
    _icon = "elastic-container-instance.png"
class ElasticHighPerformanceComputing(_Compute):
    _icon = "elastic-high-performance-computing.png"
class ElasticSearch(_Compute):
    _icon = "elastic-search.png"
class FunctionCompute(_Compute):
    _icon = "function-compute.png"
class OperationOrchestrationService(_Compute):
    _icon = "operation-orchestration-service.png"
class ResourceOrchestrationService(_Compute):
    _icon = "resource-orchestration-service.png"
class ServerLoadBalancer(_Compute):
    _icon = "server-load-balancer.png"
class ServerlessAppEngine(_Compute):
    _icon = "serverless-app-engine.png"
class SimpleApplicationServer(_Compute):
    _icon = "simple-application-server.png"
class WebAppService(_Compute):
    _icon = "web-app-service.png"

# Aliases

ESS = AutoScaling
ECS = ElasticComputeService
ECI = ElasticContainerInstance
EHPC = ElasticHighPerformanceComputing
FC = FunctionCompute
OOS = OperationOrchestrationService
ROS = ResourceOrchestrationService
SLB = ServerLoadBalancer
SAE = ServerlessAppEngine
SAS = SimpleApplicationServer
WAS = WebAppService