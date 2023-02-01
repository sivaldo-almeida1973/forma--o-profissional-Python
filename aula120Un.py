#União de Arrays
import numpy 
arr1 = numpy.array([1,2,3,4])
arr2 = numpy.array([3,4,5,6,7])
newarr = numpy.union1d(arr1,arr2)
print(newarr)

print('-'*30)
#intersecão
import numpy 
arr1 = numpy.array([1,2,3,4])
arr2 = numpy.array([3,4,5,6,7])
newarr = numpy.intersect1d(arr1,arr2)
print(newarr)


#unicos
print('-'*30)
#intersecão
import numpy 
arr1 = numpy.array([1,2,3,4,3,4,5,6,7])
newarr = numpy.unique(arr1)
print(newarr)