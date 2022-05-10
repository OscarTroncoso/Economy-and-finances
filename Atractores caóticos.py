3. #Values ​​used by formulas
4. tstop = 5.0 #end time
5. dt = 0.0001 #time jump
6.
7. #Variables of the Lorenz Equations
8. a = 5.0
9. b = 15.0
10. c = 1.0

12. #File to store the values
13. pfile = open('lorenz.dat', 'w')
14. #pfile.write("#Lorenz Attractor - lorenz.py\n")
15. #pfile.write("#a =%6.2f b =%6.2f c =%6.2f\n"%(a,b,c))

17. #Initial conditions
18. t = 0.0
19. x = 1.0
20. y = 0.0
21. z = 0.0
22. while t < tstop:
23. t = t + dt #Time plus jump
24
25. #Lorenz equations
26. dxdt = a*y - a*x
27. dydt = b*x - x*z - y
28. dzdt = x*y - c*z
29
30. #Euler approximation #working with verlet #
31. x = x + dxdt * dt
32. y = y + d and dt * dt
33. z = z + dzdt * dt

35. file write("%f%f%f%f\n" %(x,y,z,t)) #Arrange in columns
36. file close ( ) #Close the file
37.
38. #print "the file D:\Documents\lorenz.dat was written"
39.
40. #graphic
41. gnuplot << END
42. set output "Position_Time_Euler.png"
43. Title "Position Vs Time"
44. set xlabel "t(s)"
45. set and label "x (m)"
46. ​​set xrange [ 0.0 : 10.0 ]
47. p "Position_Time_Euler.dat" using 1 : 2 wp
48. ALET