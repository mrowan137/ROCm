# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import shutil
shutil.copy2('../CONTRIBUTING.md','./contributing.md')
shutil.copy2('../RELEASE.md','./release.md')


from rocm_docs import ROCmDocs

# working anchors that linkcheck cannot find
linkcheck_anchors_ignore = [
    'd90e61', 
    'd1667e113', 
    'd2999e60', 
    'building-from-source', 
    'use-the-rocm-build-tool-rbuild', 
    'use-cmake-to-build-migraphx', 
    'example'
]
linkcheck_ignore = [
    # site to be built
    "https://rocmdocs.amd.com/projects/ROCmCC/en/latest/", 
    "https://rocmdocs.amd.com/projects/RVS/en/latest/", 
    "https://rocmdocs.amd.com/projects/amdsmi/en/latest/",
    "https://rocmdocs.amd.com/projects/rdc/en/latest/",
    "https://rocmdocs.amd.com/projects/rocmsmi/en/latest/", 
    "https://rocmdocs.amd.com/projects/roctracer/en/latest/",
    "https://rocmdocs.amd.com/projects/MIGraphX/en/latest/",
    "https://rocmdocs.amd.com/projects/rocprofiler/en/latest/",
    "https://github.com/ROCm-Developer-Tools/HIP-VS/blob/master/README.md",
    "https://rocmdocs.amd.com/projects/HIPIFY/en/develop/",
    # correct links that linkcheck times out on
    r"https://www.amd.com/system/files/.*.pdf",
    "https://www.amd.com/en/developer/aocc.html",
    "https://www.amd.com/en/support/linux-drivers",
    "https://www.amd.com/en/technologies/infinity-hub",
    r"https://bitbucket.org/icl/magma/*",
    "http://cs231n.stanford.edu/"
]

html_output_directory = "../_readthedocs/html"
setting_all_article_info = True
all_article_info_os = ["linux", "windows"]
all_article_info_author = ""
all_article_info_date = "2023-05-05"
all_article_info_read_time = "5-10 min read"

# pages with specific settings
article_pages = [
    {"file":"deploy/linux/index", "os":["linux"]},
    {"file":"deploy/linux/install_overview", "os":["linux"]},
    {"file":"deploy/linux/prerequisites", "os":["linux"]},
    {"file":"deploy/linux/quick_start", "os":["linux"]},
    {"file":"deploy/linux/install", "os":["linux"]},
    {"file":"deploy/linux/upgrade", "os":["linux"]},
    {"file":"deploy/linux/uninstall", "os":["linux"]},
    {"file":"deploy/linux/package_manager_integration", "os":["linux"]},
    {"file":"deploy/docker", "os":["linux"]},
    
    {"file":"release/gpu_os_support", "os":["linux"]},
    {"file":"release/docker_support_matrix", "os":["linux"]},
    
    {"file":"reference/gpu_libraries/communication", "os":["linux"]},
    {"file":"reference/ai_tools", "os":["linux"]},
    {"file":"reference/management_tools", "os":["linux"]},
    {"file":"reference/validation_tools", "os":["linux"]},
    {"file":"reference/framework_compatibility/framework_compatibility", "os":["linux"]},
    {"file":"reference/computer_vision", "os":["linux"]},
    
    {"file":"how_to/deep_learning_rocm", "os":["linux"]},
    {"file":"how_to/gpu_aware_mpi", "os":["linux"]},
    {"file":"how_to/magma_install/magma_install", "os":["linux"]},
    {"file":"how_to/pytorch_install/pytorch_install", "os":["linux"]},
    {"file":"how_to/system_debugging", "os":["linux"]},
    {"file":"how_to/tensorflow_install/tensorflow_install", "os":["linux"]},

    {"file":"examples/ai_ml_inferencing", "os":["linux"]},
    {"file":"examples/inception_casestudy/inception_casestudy", "os":["linux"]},
    
    {"file":"understand/file_reorg", "os":["linux"]},

    {"file":"understand/isv_deployment_win", "os":["windows"]},
]

docs_core = ROCmDocs("ROCm Docs 5.6.0")
docs_core.setup()
docs_core.disable_main_doc_link()

for sphinx_var in ROCmDocs.SPHINX_VARS:
    globals()[sphinx_var] = getattr(docs_core, sphinx_var)
