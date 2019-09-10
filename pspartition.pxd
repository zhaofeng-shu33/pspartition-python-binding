from libcpp.vector cimport vector,set
from libcpp.string cimport string
ctypedef vector[int] v_i
ctypedef vector[double] v_d
cdef extern from "psp/set/set_stl.h" namespace "stl":
    cdef cppclass Set[int]:
        cppclass iterator:
            pass
        iterator begin()
        iterator end()
    cdef cppclass Partition:
        cppclass iterator:
            pass
        iterator begin()
        iterator end()
        
ctypedef vector[Partition] v_p          
cdef extern from "psp/psp.h" namespace "psp":
    cdef cppclass PSP:
        PSP(v_i, v_i, v_d, int) except +
        v_d get_critical_values()
        v_p get_partitions()
        void run(string)

      
