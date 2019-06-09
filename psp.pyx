# distutils: language = c++
from libcpp.vector cimport vector
from info_cluster cimport InfoCluster
ctypedef vector[int] v_i
ctypedef vector[double] v_d 
cdef class PyGraph:
    cdef InfoCluster* ic
    
    def __init__(self, num_points, py_list):
        cdef v_i s_list, t_list
        cdef v_d weight_list
        for i,j,k in py_list:
            s_list.push_back(i)
            t_list.push_back(j)
            weight_list.push_back(k)
            
        self.ic = new InfoCluster(s_list, t_list, weight_list, num_points)

    def __dealloc__(self):
        del self.ic
        
    def get_critical_values(self):
        return self.ic.get_critical_value_vector()
        
    def get_partitions(self):
        return self.ic.get_partitions()
        
    def run(self):
        self.ic.run()
    
    def get_category(self, i):
        return self.ic.get_category(i)