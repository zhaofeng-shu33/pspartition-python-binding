# distutils: language = c++
from libcpp.string cimport string
from libcpp.vector cimport vector
from pspartition cimport PSP
cdef extern from "psp/psp/version.h":
    double PSP_VERSION_MAJOR
__version__ = PSP_VERSION_MAJOR
cdef class PsPartition:
    cdef PSP* psp
    
    def __init__(self, num_points, py_list):
        cdef v_i s_list, t_list
        cdef v_d weight_list
        for i,j,k in py_list:
            s_list.push_back(i)
            t_list.push_back(j)
            weight_list.push_back(k)
            
        self.psp = new PSP(s_list, t_list, weight_list, num_points)

    def __dealloc__(self):
        del self.psp
        
    def get_critical_values(self):
        return self.psp.get_critical_values()
        
    def get_partitions(self):
        cdef v_p v_p_instance
        v_p_instance = self.psp.get_partitions()
        py_partition_list = []
        for partition_instance in v_p_instance:
            py_partition = []
            for set_instance in partition_instance:
                py_set = set()
                for i in set_instance:
                    py_set.add(i)
                py_partition.append(py_set)
            py_partition_list.append(py_partition)
            
    def run(self, py_method_name='psp_i'):
        cdef string method = py_method_name.encode('ascii')
        self.psp.run(method)
        

        
