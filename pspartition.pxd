from libcpp.vector cimport vector
from libcpp.string cimport string
ctypedef vector[int] v_i
ctypedef vector[double] v_d
cdef extern from "psp/psp.h" namespace "psp":
    cdef cppclass PSP:
        PSP(v_i, v_i, v_d, int) except +
        v_d get_critical_values()
        #v_i get_partitions()
        void run(string)
        
