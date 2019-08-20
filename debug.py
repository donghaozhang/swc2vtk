import swc2vtk
vtkgen = swc2vtk.VtkGenerator()

vtkgen.set_draw_mode(1)
vtkgen.add_swc('./swc/simple.swc')
# vtkgen.write_vtk('simple.vtk')
#
# vtkgen = swc2vtk.VtkGenerator()
# vtkgen.add_swc('./swc/simple.swc')
# vtkgen.add_swc('./swc/simple.swc')
# vtkgen.add_swc('./swc/simple.swc')
# vtkgen.write_vtk('combined.vtk')
#
# import swc2vtk
# vtkgen = swc2vtk.VtkGenerator()
# vtkgen.add_swc('./swc/simple.swc')
#
# vtkgen.add_datafile('result1.dat')
# vtkgen.write_vtk('./swc/simple1.vtk')
#
# vtkgen.clear_datafile()
# vtkgen.add_datafile('result2.dat')
# vtkgen.write_vtk('simple2.vtk')
#
# vtkgen.clear_datafile()
# vtkgen.add_datafile('result3.dat')
# vtkgen.write_vtk('simple3.vtk')