# flake8: noqa

if __import__("typing").TYPE_CHECKING:
    # import apis into api package
    from oden.api.intervals_api import IntervalsApi
    from oden.api.machine_groups_api import MachineGroupsApi
    from oden.api.metric_groups_api import MetricGroupsApi
    from oden.api.oql_api import OQLApi
    from oden.api.product_attributes_api import ProductAttributesApi
    from oden.api.product_mappings_api import ProductMappingsApi
    from oden.api.products_api import ProductsApi
    from oden.api.quality_test_api import QualityTestApi
    from oden.api.scrap_yield_data_api import ScrapYieldDataApi
    from oden.api.targets_api import TargetsApi
    
else:
    from lazy_imports import LazyModule, as_package, load

    load(
        LazyModule(
            *as_package(__file__),
            """# import apis into api package
from oden.api.intervals_api import IntervalsApi
from oden.api.machine_groups_api import MachineGroupsApi
from oden.api.metric_groups_api import MetricGroupsApi
from oden.api.oql_api import OQLApi
from oden.api.product_attributes_api import ProductAttributesApi
from oden.api.product_mappings_api import ProductMappingsApi
from oden.api.products_api import ProductsApi
from oden.api.quality_test_api import QualityTestApi
from oden.api.scrap_yield_data_api import ScrapYieldDataApi
from oden.api.targets_api import TargetsApi

""",
            name=__name__,
            doc=__doc__,
        )
    )
