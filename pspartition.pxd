from libcpp.vector cimport vector,set
from libcpp.string cimport string
ctypedef vector[int] v_i
ctypedef vector[double] v_d
cdef extern from "psp/set/set_stl.h" namespace "stl":
    cdef cppclass CSet:
        cppclass iterator:
            int& operator*()
            iterator operator++()
            bint operator!=(iterator)
        iterator begin()
        iterator end()
    cdef cppclass Partition:
        cppclass iterator:
            CSet& operator*()
            iterator operator++()
            bint operator!=(iterator)
        iterator begin()
        iterator end()
ctypedef vector[Partition] v_p          
cdef extern from "psp/psp.h" namespace "psp":
    cdef cppclass PSP:
        PSP(v_i, v_i, v_d, int) except +
        v_d get_critical_values()
        v_p get_partitions()
        void run(string) except +

      
