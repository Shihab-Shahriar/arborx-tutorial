# Visualizing ArborX

This example contains several ways to visualize the internals of ArborX tree structure and traversal. This buiilds on the official ArborX vizualization example, expands on it in many ways since that example still remains incomplete.  

+ To compile and generate vizualization data: 
    + Load the usual modules. 
    + `cmake .`
    + `make`
    + `./ArborX_TreeViz.exe`

The executable reads 58 points from `leaf_cloud.txt`, constructs BVH tree and performs queries for each point to find their K nearest neighbors (default 5). It captures the tree strcuture and traversal data with the help of several undocumented functions in `ArborX_DetailsTreeTraversal.hpp` file. This will generate lots of visualization data in .m4 format. We can use simple python scripts to take that data and vizualize them.

+ To print out the constructed tree and the bounding volumes, please refer to `visualize_tree.ipynb` IPython notebook.

+ To generate traversal matrix, which helps illustrate how sorting the (batched) queries can improve data and code execution locality: run `arborx_query_sort.py` script.
    + As example, `python arborx_query_sort.py -a shuffled -p viz_` to generate traversed leaves when queries are shuffled, and `python arborx_query_sort.py -a sorted -p viz_` when queries are sorted based on a locality aware hashing technique (morton code). This will generate shuffled.png and sorted.png respectively.