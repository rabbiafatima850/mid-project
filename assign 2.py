healthcare_diagnostics=input('enter your problem :')
#for headache.
if healthcare_diagnostics=='headache':
     print ('flu')
#for eye problem.
elif healthcare_diagnostics=='eye burning':
     print ('eye infection')
#for chest pain.
elif healthcare_diagnostics  =='chest pain':
     print( 'angina')
#for throat problem.
elif healthcare_diagnostics=='throat':
     print('tonsils')
#for lung infection.
elif healthcare_diagnostics=='lung infection':
     print('pneumonia')
#for acidity.
elif healthcare_diagnostics=='acidity':
     print('stomach-problem')
#for diarrhea.
elif healthcare_diagnostics=='diarrhea':
     print('infection or wound in intestine')
else:
    print ('healthy')

print(healthcare_diagnostics) 
 