from libcpp.vector cimport vector
ctypedef vector[int] v_i
ctypedef vector[double] v_d
cdef extern from "core/graph/info_cluster.h" namespace "submodular":
    cdef cppclass InfoCluster:
        InfoCluster(v_i, v_i, v_d, int) except +
        v_d get_critical_value_vector()
        v_i get_partitions()
        void run()
        v_i get_category(int)
        v_i get_labels(int)
        void run_pdt()
        void run_psp_i()
        
cdef extern from "core/graph/gaussian2Dcase.h" namespace "demo":        
    cdef cppclass Gaussian2DGraph:
        Gaussian2DGraph(int, double) except +
        v_d get_x_pos_list()
        v_d get_y_pos_list()
        v_d get_critical_value_vector()        
        v_i get_partitions()
        void run()
        v_i get_category(int)