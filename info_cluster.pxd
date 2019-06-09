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
