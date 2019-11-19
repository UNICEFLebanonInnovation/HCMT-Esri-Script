
import arcpy
from arcgis.gis import GIS
from IPython.display import display


def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False

FeaturesToUpdate = []

#print('Connecting to feature layer')
gis = GIS("http://uniceflebanon.maps.arcgis.com", "", "")
search_result = gis.content.get('')
print("Feature Layer Connected")
#myFLayer = search_result[0]
#layers = myFLayer.layers
neededLayer = search_result.layers[0]
#print("getting the needed sub layer (/0)")
pFeatureSet = neededLayer.query(where="Report_AI is null and site_currently_empty = 'no' and permission ='yes'")
existingFeatures = pFeatureSet.features
print("looping into features...")
#fieldsList = neededLayer.properties.fields
#print(fieldsList)
#print("#############################")
#Looping "for" in all sites
for feature in existingFeatures:
  Report_AI=feature.attributes["Report_AI"]#calling Report_AI field
  #site_currently_empty=feature.attributes["site_currently_empty"]
  #permission=feature.attributes["permission"]
  #if site_currently_empty=='yes' or permission=='no':
    #continue
    #print("continue in")
  #if not Report_AI:
    #Report_AI=""
  #if Report_AI=="":#check if report is empty to do the calculation else go to the next record
    #print("report is empty to be calculated")
  n=1
  ##Average variables 
  avg_hands_washed_HH=[]
  avg_disease_prevention_HH=[]
  avg_source_drinking_HH=[]
  avg_latrine_cleanliness_HH=[]
  avg_latrine_functionality_HH=[]
  avg_latrine_lock_HH=[]
  avg_latrine_light_HH=[]
  avg_solid_waste=0
  avg_latrine_privacy_HH=[]
  avg_hands_washed_HH_V=0
  avg_happy_HH=[]
  #Protection variables 
  prot_women=0
  prot_men=0
  prot_girls=0
  prot_boys=0
  Cprot_sani_women_LP=0
  Cprot_sani_women_SV=0
  Cprot_sani_women_LD=0
  Cprot_sani_women_DW=0
  Cprot_sani_women_NC=0
  Cprot_sani_women_SN=0
  Cprot_sani_women_LL =0
  Cprot_sani_women_NO=0
  Cprot_water_women_SV=0
  Cprot_water_women_LP=0
  Cprot_water_women_LD=0
  Cprot_water_women_LL=0
  Cprot_water_women_DW=0
  Cprot_water_women_NC=0
  Cprot_water_women_SN=0
  Cprot_water_women_NO=0
  Cprot_sani_girls_LP=0
  Cprot_sani_girls_SV=0
  Cprot_sani_girls_LD=0
  Cprot_sani_girls_LL=0
  Cprot_sani_girls_DW=0
  Cprot_sani_girls_NC=0
  Cprot_sani_girls_SN=0
  Cprot_sani_girls_NO=0
  Cprot_water_girls_LP=0
  Cprot_water_girls_SV=0
  Cprot_water_girls_LD=0
  Cprot_water_girls_LL=0
  Cprot_water_girls_DW=0
  Cprot_water_girls_NC=0
  Cprot_water_girls_SN=0
  Cprot_water_girls_NO=0
  Cprot_sani_men_LP=0
  Cprot_sani_men_SV=0
  Cprot_sani_men_LD=0
  Cprot_sani_men_LL=0
  Cprot_sani_men_DW=0
  Cprot_sani_men_NC=0
  Cprot_sani_men_SN=0
  Cprot_sani_men_NO=0
  Cprot_water_men_LP=0
  Cprot_water_men_SV=0
  Cprot_water_men_LD=0
  Cprot_water_men_LL=0
  Cprot_water_men_DW=0
  Cprot_water_men_NC=0
  Cprot_water_men_SN=0
  Cprot_water_men_NO=0
  Cprot_sani_boys_LP=0
  Cprot_sani_boys_SV=0
  Cprot_sani_boys_LD=0
  Cprot_sani_boys_LL=0
  Cprot_sani_boys_DW=0
  Cprot_sani_boys_NC=0
  Cprot_sani_boys_SN=0
  Cprot_sani_boys_NO=0
  Cprot_water_boys_LP=0
  Cprot_water_boys_SV=0
  Cprot_water_boys_LD=0
  Cprot_water_boys_LL=0
  Cprot_water_boys_DW=0
  Cprot_water_boys_NC=0
  Cprot_water_boys_SN=0
  Cprot_water_boys_NO=0
  ###Total
  total_protection_san=0
  total_protection_water=0
  ###counts
  count_hand_washed=0
  count_disease_prevention=0
  count_solid_waste=0
  count_source_drinking=0
  ##Scores##
  open_defecation_score=0
  clean_environment_score=0
  free_res_tank_score=0
  free_res_HH_score=0
  total_source_drinking=0
  total_solid_waste=0
  protection_san_score=0
  protection_water_score=0
  count_sani_all_issues=0
  count_water_all_issues=0
  sample_tents=feature.attributes["sample_tents"]#calling sample tents  field that will be the condition to compare in while loop
  #Checking if value is Null to put space instead of zero since zero is a value 
  if not sample_tents:
    sample_tents=""
    #"While" Looping in all households per site
  while (n<=sample_tents):
    total_source_drinking=0
    count_source_drinking=0
    count_disease_prevention=0
    gender_respondent_HH=feature.attributes["gender_respondent_HH" + str(n)]#calling gender field
    if not gender_respondent_HH:
          gender_respondent_HH=""
    age_respondednt_HH=feature.attributes["age_respondednt_HH" + str(n)]#calling age field
    if not age_respondednt_HH:
        age_respondednt_HH=""
    sanitation_safty_HH=feature.attributes["sanitation_safty_HH" + str(n)]#calling sanitation safty chosen by user multiple choice
    if not sanitation_safty_HH:
        sanitation_safty_HH=""
    water_safty_HH=feature.attributes["water_safty_HH" + str(n)]#calling water chosen by user multiple choice
    if not water_safty_HH:
        water_safty_HH=""
    open_defecation=feature.attributes["open_defecation"]#calling open defecation field
    if not open_defecation:
        open_defecation=""
    clean_environment=feature.attributes["clean_environment"]#calling clean environment field
    if not clean_environment:
        clean_environment=""
    chlorine_test_result1=feature.attributes["chlorine_test_result1"]#calling chlorine_test_result1 field
    if not chlorine_test_result1:
        chlorine_test_result1=""
    chlorine_test_result2=feature.attributes["chlorine_test_result2"]#calling chlorine_test_result2 fiel
    if not chlorine_test_result2:
        chlorine_test_result2=""
    hands_washed_HH=feature.attributes["hands_washed_HH" + str(n)]#calling hands washed field
    if not hands_washed_HH:
        hands_washed_HH=""
    disease_prevention_HH=feature.attributes["disease_prevention_HH" + str(n)]#calling disease prevention field
    if not disease_prevention_HH:
        disease_prevention_HH=""
    access_to_safe_drinking_water_HH=feature.attributes["access_to_safe_drinking_water_HH" + str(n)]#calling access to safe drinking field
    if not access_to_safe_drinking_water_HH:
        access_to_safe_drinking_water_HH=""
    latrine_cleanliness_HH=feature.attributes["latrine_cleanliness_HH" + str(n)]#calling latrine cleanliness field/Is the latrine clean/hygienic?
    if not latrine_cleanliness_HH:
        latrine_cleanliness_HH=""
    latrine_functionality_HH=feature.attributes["latrine_functionality_HH" + str(n)]#calling latrine functionality fiel
    if not latrine_functionality_HH:
        latrine_functionality_HH=""
    latrine_lock_HH=feature.attributes["latrine_lock_HH" + str(n)]#calling latrine lock field
    if not latrine_lock_HH:
        latrine_lock_HH=""
    latrine_light_HH =feature.attributes["latrine_light_HH" + str(n)] #calling latrine lock score field
    if not latrine_light_HH:
        latrine_light_HH=""
    latrine_privacy_HH =feature.attributes["latrine_privacy_HH" + str(n)] #calling latrine lock score field
    if not latrine_privacy_HH:
        latrine_privacy_HH=""
    solid_waste_disposal=feature.attributes["solid_waste_disposal"]#calling solid waste disposal field
    if not solid_waste_disposal:
        solid_waste_disposal=""
    confirm_partner=feature.attributes["confirm_partner"]#calling confirm partner field
    if not confirm_partner:
      confirm_partner=""
    happy_HH=feature.attributes["happy_HH" + str(n)]#calling happy partner field
    if not happy_HH:
      happy_HH=""
    #####################start conditioning protection (Sanitation & Water )##################
    if gender_respondent_HH == 'female':#calculating female
      if age_respondednt_HH>=18: # >= women
        prot_women+=1
        #checking sanitation safty women
        #Since there might be multiple choices we use split 
        if 'lack_of_privacy'in sanitation_safty_HH.split(","):#checking if lack of privacy exist
           Cprot_sani_women_LP+= 1#counting nb of lack of privacy sanitation for women
        if 'fear_sexual_violence'in sanitation_safty_HH.split(","):
          Cprot_sani_women_SV+=1
        if 'lack_proper_locks'in sanitation_safty_HH.split(","):
                        Cprot_sani_women_LD+= 1
        if 'little_no_light'in sanitation_safty_HH.split(","):
                        Cprot_sani_women_LL+= 1
        if 'distance_to_latrines'in sanitation_safty_HH.split(","):
                        Cprot_sani_women_DW+= 1
        if 'not_comfortable'in sanitation_safty_HH.split(","):
                        Cprot_sani_women_NC+= 1
        if 'special_needs'in sanitation_safty_HH.split(","):
                        Cprot_sani_women_SN+= 1
        if 'no_issues'in sanitation_safty_HH.split(","): 
                        Cprot_sani_women_NO+=1
                        protection_san_score+=100
                        count_sani_all_issues+=1
                    #checking water safty women
        if 'lack_of_privacy'in water_safty_HH.split(","):
                        #checking if lack of privacy exist
                        Cprot_water_women_LP+= 1#counting nb of lack of privacy water for women
        if 'fear_sexual_violence'in water_safty_HH.split(","):
                                Cprot_water_women_SV+=1
        if 'lack_proper_locks'in water_safty_HH.split(","):
                                Cprot_water_women_LD+= 1
        if 'little_no_light'in water_safty_HH.split(","):
                                Cprot_water_women_LL+= 1
        if 'distance_to_water'in water_safty_HH.split(","):
                                Cprot_water_women_DW+= 1
        if 'not_comfortable'in water_safty_HH.split(","):
                                Cprot_water_women_NC+= 1
        if 'special_needs'in water_safty_HH.split(","):
                                Cprot_water_women_SN+= 1
        if 'no_issues'in water_safty_HH.split(","):
                                Cprot_water_women_NO+=1
                                protection_water_score+=100
                                count_water_all_issues+=1

      else:
        prot_girls+=1 # <18 girls
        #checking sanitation safty girls
        if 'lack_of_privacy'in sanitation_safty_HH.split(","):#checking if lack of privacy exist 
                                 Cprot_sani_girls_LP+= 1#counting nb of lack of privacy sanitation for girls
        if 'fear_sexual_violence'in sanitation_safty_HH.split(","):
                                 Cprot_sani_girls_SV+=1
        if 'lack_proper_locks'in sanitation_safty_HH.split(","):
                                 Cprot_sani_girls_LD+= 1
        if 'little_no_light'in sanitation_safty_HH.split(","):
                                 Cprot_sani_girls_LL+= 1
        if 'distance_to_latrines'in sanitation_safty_HH.split(","):
                                 Cprot_sani_girls_DW+= 1
        if 'not_comfortable'in sanitation_safty_HH.split(","):
                                 Cprot_sani_girls_NC+= 1
        if 'special_needs'in sanitation_safty_HH.split(","):
                                Cprot_sani_girls_SN+= 1
        if 'no_issues'in sanitation_safty_HH.split(","):
                                 Cprot_sani_girls_NO+=1
                                 protection_san_score+=100
                                 count_sani_all_issues+=1
                        #checking water safty girls
        if 'lack_of_privacy'in water_safty_HH.split(","):#checking if lack of privacy exist 
                                  Cprot_water_girls_LP+= 1#counting nb of lack of privacy water for girls
        if 'fear_sexual_violence'in water_safty_HH.split(","):
                                  Cprot_water_girls_SV+=1
        if 'lack_proper_locks'in water_safty_HH.split(","):
                                  Cprot_water_girls_LD+= 1
        if 'little_no_light'in water_safty_HH.split(","):
                                  Cprot_water_girls_LL+= 1
        if 'distance_to_water'in water_safty_HH.split(","):
                                  Cprot_water_girls_DW+= 1
        if 'not_comfortable'in water_safty_HH.split(","):
                                  Cprot_water_girls_NC+= 1
        if 'special_needs'in water_safty_HH.split(","):
                                  Cprot_water_girls_SN+= 1
        if 'no_issues'in water_safty_HH.split(","):
                                  Cprot_water_girls_NO+=1
                                  protection_water_score+=100
                                  count_water_all_issues+=1
    elif  gender_respondent_HH=='male':#calculating male
        if age_respondednt_HH>=18: # >= men
          prot_men+=1
          #checking sanitation safty men
          if 'lack_of_privacy'in sanitation_safty_HH.split(","):#checking if lack of privacy exist
            Cprot_sani_men_LP+= 1#counting nb of lack of privacy sanitation for men
          if 'fear_sexual_violence'in sanitation_safty_HH.split(","):
            Cprot_sani_men_SV+=1
          if 'lack_proper_locks'in sanitation_safty_HH.split(","):
            Cprot_sani_men_LD+= 1
          if 'little_no_light'in sanitation_safty_HH.split(","):
            Cprot_sani_men_LL+= 1
          if 'distance_to_latrines'in sanitation_safty_HH.split(","):
            Cprot_sani_men_DW+= 1
          if 'not_comfortable'in sanitation_safty_HH.split(","):
            Cprot_sani_men_NC+= 1
          if 'special_needs'in sanitation_safty_HH.split(","):
            Cprot_sani_men_SN+= 1
          if 'no_issues'in sanitation_safty_HH.split(","):
            Cprot_sani_men_NO+=1
            protection_san_score+=100
            count_sani_all_issues+=1
                    #checking water safty men
          if 'lack_of_privacy'in water_safty_HH.split(","):#checking if lack of privacy exist 
                              Cprot_water_men_LP+= 1#counting nb of lack of privacy water for men
          if 'fear_sexual_violence'in water_safty_HH.split(","):
                              Cprot_water_men_SV+=1
          if 'lack_proper_locks'in water_safty_HH.split(","):
                              Cprot_water_men_LD+= 1
          if 'little_no_light'in water_safty_HH.split(","):
                              Cprot_water_men_LL+= 1
          if 'distance_to_water'in water_safty_HH.split(","):
                              Cprot_water_men_DW+= 1
          if 'not_comfortable'in water_safty_HH.split(","):
                              Cprot_water_men_NC+= 1
          if 'special_needs'in water_safty_HH.split(","):
                              Cprot_water_men_SN+= 1
          if 'no_issues'in water_safty_HH.split(","):
                              Cprot_water_men_NO+=1
                              protection_water_score+=100
                              count_water_all_issues+=1
        else:
          prot_boys+=1 # < 18 boys
          #checking sanitation safty boys
          if 'lack_of_privacy'in sanitation_safty_HH.split(","):#checking if lack of privacy exist 
                                 Cprot_sani_boys_LP+= 1#counting nb of lack of privacy sanitation  for boys
          if 'fear_sexual_violence'in sanitation_safty_HH.split(","):
                                 Cprot_sani_boys_SV+=1
          if 'lack_proper_locks'in sanitation_safty_HH.split(","):
                                 Cprot_sani_boys_LD+= 1
          if 'little_no_light'in sanitation_safty_HH.split(","):
                                 Cprot_sani_boys_LL+= 1
          if 'distance_to_latrines'in sanitation_safty_HH.split(","):
                                 Cprot_sani_boys_DW+= 1
          if 'not_comfortable'in sanitation_safty_HH.split(","):
                                 Cprot_sani_boys_NC+= 1
          if 'special_needs'in sanitation_safty_HH.split(","):
                                 Cprot_sani_boys_SN+= 1
          if 'no_issues'in sanitation_safty_HH.split(","):
                                Cprot_sani_boys_NO+=1
                                protection_san_score+=100
                                count_sani_all_issues+=1
                                #checking water safty boys
          if 'lack_of_privacy'in water_safty_HH.split(","): #checking if lack of privacy exist
                                 Cprot_water_boys_LP+= 1 #counting nb of lack of privacy water for boys
          if 'fear_sexual_violence'in water_safty_HH.split(","):
            Cprot_water_boys_SV+=1
          if 'lack_proper_locks'in water_safty_HH.split(","):
            Cprot_water_boys_LD+= 1
          if 'little_no_light'in water_safty_HH.split(","):
            Cprot_water_boys_LL+= 1
          if 'distance_to_water'in water_safty_HH.split(","):
            Cprot_water_boys_DW+= 1
          if 'not_comfortable'in water_safty_HH.split(","):
            Cprot_water_boys_NC+= 1
          if 'special_needs'in water_safty_HH.split(","):
            Cprot_water_boys_SN+= 1
          if 'no_issues'in water_safty_HH.split(","):
                                 Cprot_water_boys_NO+=1
                                 protection_water_score+=100
                                 count_water_all_issues+=1
      

      #########checking hand washing ########
    if 'before_eating'in hands_washed_HH.split(","):#counting when washing hands is done
          count_hand_washed+=1
    if 'before_feeding'in hands_washed_HH.split(","):
           count_hand_washed+=1
    if 'before_handling'in hands_washed_HH.split(","):
          count_hand_washed+=1
    if 'after_toilet'in hands_washed_HH.split(","):
          count_hand_washed+=1
    if 'after_diapers'in hands_washed_HH.split(","):
          count_hand_washed+=1    
    if 'unknown'in hands_washed_HH.split(","):
      avg_hands_washed_HH.append(avg_hands_washed_HH_V)#append is to add the values to an array
      #append is to add the values to an array 
    avg_hands_washed_HH.append(count_hand_washed*100/3)#average hands washed  per household count of selection
    count_hand_washed=0
              #conditions on avg hands washed per household
    if avg_hands_washed_HH[len(avg_hands_washed_HH)-1]>=100:
      avg_hands_washed_HH[len(avg_hands_washed_HH)-1]=100
    elif  avg_hands_washed_HH[len(avg_hands_washed_HH)-1]<100:
      avg_hands_washed_HH[len(avg_hands_washed_HH)-1]=avg_hands_washed_HH[len(avg_hands_washed_HH)-1]#if result < 100 the value is equal to the result		
              #fill in Disease_prevention_score options multiple choices
    if 'handwashing'in disease_prevention_HH.split(","):
                            count_disease_prevention+=1#counting selection
    if 'clean_water'in disease_prevention_HH.split(","):
                                    count_disease_prevention+=1
    if 'use_latrines'in disease_prevention_HH.split(","):
                                    count_disease_prevention+=1
    if 'food_hygiene'in disease_prevention_HH.split(","):
                                    count_disease_prevention+=1
    if 'unknown'in disease_prevention_HH.split(","):
        avg_disease_prevention_HH.append(0) #if option is unknown score is 0
    avg_disease_prevention_HH.append(count_disease_prevention*100/2)#average disease prevention per household nb of selection
            #conditions on avg disease preventoin per household
    if avg_disease_prevention_HH[len(avg_disease_prevention_HH)-1] >=100:
          avg_disease_prevention_HH[len(avg_disease_prevention_HH)-1]=100
    elif  avg_disease_prevention_HH[len(avg_disease_prevention_HH)-1]<100:
          avg_disease_prevention_HH[len(avg_disease_prevention_HH)-1]=avg_disease_prevention_HH[len(avg_disease_prevention_HH)-1]
             # fill in source_drinking_score options multiple choices
    if 'hh_treated'in access_to_safe_drinking_water_HH.split(","):
      count_source_drinking+=1
      total_source_drinking+=100
    if 'bottled'in access_to_safe_drinking_water_HH.split(",") :
      count_source_drinking+=1
      total_source_drinking+=100
    if 'filtered_water'in access_to_safe_drinking_water_HH.split(","):
      count_source_drinking+=1
      total_source_drinking+=100
    if 'we_public_network'in access_to_safe_drinking_water_HH.split(","):
      count_source_drinking+=1
      total_source_drinking+=100
    if 'not_treated'in access_to_safe_drinking_water_HH.split(","):
      count_source_drinking+=1
    if 'irrigation_pipe'in access_to_safe_drinking_water_HH.split(",") :
      count_source_drinking+=1
    if 'water_trucking'in access_to_safe_drinking_water_HH.split(","):
      count_source_drinking+=1
    if 'water_trucking_1'in access_to_safe_drinking_water_HH.split(","):
      count_source_drinking+=1
    if 'mixing_water'in access_to_safe_drinking_water_HH.split(","):
      count_source_drinking+=1
    if 'unknown'in access_to_safe_drinking_water_HH.split(","):
      count_source_drinking+=1
    avg_source_drinking_HH.append(total_source_drinking/count_source_drinking) #average source drinking water per household
             #conditions on average source drinking per household 
    if avg_source_drinking_HH[len(avg_source_drinking_HH)-1]>=100:
      avg_source_drinking_HH[len(avg_source_drinking_HH)-1]=100
    elif  avg_source_drinking_HH[len(avg_source_drinking_HH)-1]<100:
      avg_source_drinking_HH[len(avg_source_drinking_HH)-1]=avg_source_drinking_HH[len(avg_source_drinking_HH)-1]
            # fill in clean_latrine_score (is the latrine clean/hygine?)
    if latrine_cleanliness_HH.lower()=='clean':
      avg_latrine_cleanliness_HH.append(100)
    elif latrine_cleanliness_HH.lower()=='not_clean':
      avg_latrine_cleanliness_HH.append(0)
    elif latrine_cleanliness_HH.lower()=='clean_somewhat':
      avg_latrine_cleanliness_HH.append(50)
                             # fill in fun_latrine_score
    if latrine_functionality_HH=='Functional':
                       avg_latrine_functionality_HH.append(100)
    elif latrine_functionality_HH=='Not functional':
                       avg_latrine_functionality_HH.append(0)
                     # fill in lock_latrine_score
    if latrine_lock_HH=='yes':
                       avg_latrine_lock_HH.append(100)
    else:
      avg_latrine_lock_HH.append(0)
                     # fill in light_latrine_score
    if latrine_light_HH=='yes':
                       avg_latrine_light_HH.append(100)
    else:
      avg_latrine_light_HH.append(0)
        #fill in look latrine score (privacy)
    if latrine_privacy_HH=='no':
      avg_latrine_privacy_HH.append(0)
    else:
          avg_latrine_privacy_HH.append(100)
      ######fill in happy partner######
   # print(happy_HH)
    if happy_HH.lower()=='yes':
      avg_happy_HH.append(100)
     # print("happy is 100")
    else:#else if happy = no or happy= n/a
     # print("happy 0")
      avg_happy_HH.append(0)    
    #print("next HH")
    n+=1
      #fill in open defectation score
  if open_defecation == 'yes':
      open_defecation_score=100   
  else:
      open_defecation_score=0	   
  #fill in clean_environment_score
  if clean_environment =='yes':
      clean_environment_score=100
  else:
      clean_environment_score=0
  #fill in free_res_tank_score
################# Check if field is a number ######################
  if isfloat(chlorine_test_result1):        
      if chlorine_test_result1<0.2 or chlorine_test_result1>0.5:
          free_res_tank_score=0
      elif chlorine_test_result1>= 0.2 and chlorine_test_result1<=0.5:
          free_res_tank_score=100
  #fill in free_res_HH_score
  if isfloat(chlorine_test_result2):   
    if chlorine_test_result2<0.2 or chlorine_test_result2>0.5:
        free_res_HH_score=0
    elif chlorine_test_result2>=0.2 and chlorine_test_result2<=0.5:
         free_res_HH_score=100
  #fill in solid_waste_score
  if 'waste_is_sorted' in solid_waste_disposal.split(","):
      count_solid_waste+=1
      total_solid_waste+=100
  if 'waste_is_disposed' in solid_waste_disposal.split(","):
      count_solid_waste+=1
      total_solid_waste+=100
  if 'waste_is_dumped' in solid_waste_disposal.split(","):
      count_solid_waste+=1
  if 'waste_is_dumped_around' in solid_waste_disposal.split(","):
      count_solid_waste+=1
  if 'waste_is_burned' in solid_waste_disposal.split(","):
      count_solid_waste+=1
  if 'waste_is_dumped_random' in solid_waste_disposal.split(","):
      count_solid_waste+=1
  if 'unknown' in solid_waste_disposal.split(","):
      count_solid_waste+=1
  if(count_solid_waste == 0):
      count_solid_waste=1
  avg_solid_waste=total_solid_waste/count_solid_waste #average solid waste for all households
  
  #conditions on avg solid waste
  if avg_solid_waste>=100:
   solid_waste_score=100
  else:
    solid_waste_score=avg_solid_waste
    #fill in partner_knowledge score
  if confirm_partner == 'yes':
        partner_knowledge=100	
  else:
        partner_knowledge=0
 # print("confirm:",confirm_partner)
  ##################### Calculating Protection ##################################
  #calculating women sanitation
  if(prot_women ==0):
      prot_sani_women_LP=0
      prot_sani_women_SV=0
      prot_sani_women_LD=0
      prot_sani_women_LL=0
      prot_sani_women_DW=0
      prot_sani_women_NC=0
      prot_sani_women_SN=0
      prot_sani_women_NO=0
  else:
      prot_sani_women_LP=Cprot_sani_women_LP*100/prot_women
      prot_sani_women_SV=Cprot_sani_women_SV*100/prot_women
      prot_sani_women_LD=Cprot_sani_women_LD*100/prot_women
      prot_sani_women_LL=Cprot_sani_women_LL*100/prot_women
      prot_sani_women_DW=Cprot_sani_women_DW*100/prot_women
      prot_sani_women_NC=Cprot_sani_women_NC*100/prot_women
      prot_sani_women_SN=Cprot_sani_women_SN*100/prot_women
      prot_sani_women_NO=Cprot_sani_women_NO*100/prot_women
  #calculating girls sanitation
  if(prot_girls ==0):
      prot_sani_girls_LP=0
      prot_sani_girls_SV=0
      prot_sani_girls_LD=0
      prot_sani_girls_LL=0
      prot_sani_girls_DW=0
      prot_sani_girls_NC=0
      prot_sani_girls_SN=0
      prot_sani_girls_NO=0
  else:
      prot_sani_girls_LP=Cprot_sani_girls_LP*100/prot_girls
      prot_sani_girls_SV=Cprot_sani_girls_SV*100/prot_girls
      prot_sani_girls_LD=Cprot_sani_girls_LD*100/prot_girls
      prot_sani_girls_LL=Cprot_sani_girls_LL*100/prot_girls
      prot_sani_girls_DW=Cprot_sani_girls_DW*100/prot_girls
      prot_sani_girls_NC=Cprot_sani_girls_NC*100/prot_girls
      prot_sani_girls_SN=Cprot_sani_girls_SN*100/prot_girls
      prot_sani_girls_NO=Cprot_sani_girls_NO*100/prot_girls
  #calculating men sanitation
  if(prot_men ==0):
      prot_sani_men_LP=0
      prot_sani_men_SV=0
      prot_sani_men_LD=0
      prot_sani_men_LL=0
      prot_sani_men_DW=0
      prot_sani_men_NC=0
      prot_sani_men_SN=0
      prot_sani_men_NO=0
  else:
      prot_sani_men_LP=Cprot_sani_men_LP*100/prot_men
      prot_sani_men_SV=Cprot_sani_men_SV*100/prot_men
      prot_sani_men_LD=Cprot_sani_men_LD*100/prot_men
      prot_sani_men_LL=Cprot_sani_men_LL*100/prot_men
      prot_sani_men_DW=Cprot_sani_men_DW*100/prot_men
      prot_sani_men_NC=Cprot_sani_men_NC*100/prot_men
      prot_sani_men_SN=Cprot_sani_men_SN*100/prot_men
      prot_sani_men_NO=Cprot_sani_men_NO*100/prot_men
  #calculating boys sanitation
  if(prot_boys ==0):
      prot_sani_boys_LP=0
      prot_sani_boys_SV=0
      prot_sani_boys_LD=0
      prot_sani_boys_LL=0
      prot_sani_boys_DW=0
      prot_sani_boys_NC=0
      prot_sani_boys_SN=0
      prot_sani_boys_NO=0
  else:
      prot_sani_boys_LP=Cprot_sani_boys_LP*100/prot_boys
      prot_sani_boys_SV=Cprot_sani_boys_SV*100/prot_boys
      prot_sani_boys_LD=Cprot_sani_boys_LD*100/prot_boys
      prot_sani_boys_LL=Cprot_sani_boys_LL*100/prot_boys
      prot_sani_boys_DW=Cprot_sani_boys_DW*100/prot_boys
      prot_sani_boys_NC=Cprot_sani_boys_NC*100/prot_boys
      prot_sani_boys_SN=Cprot_sani_boys_SN*100/prot_boys
      prot_sani_boys_NO=Cprot_sani_boys_NO*100/prot_boys
  #####
  #calculating women water safty
  if(prot_women ==0):
      prot_water_women_LP=0
      prot_water_women_SV=0
      prot_water_women_LD=0
      prot_water_women_LL=0
      prot_water_women_DW=0
      prot_water_women_NC=0
      prot_water_women_SN=0
      prot_water_women_NO=0
  else:
      prot_water_women_LP=Cprot_water_women_LP*100/prot_women
      prot_water_women_SV=Cprot_water_women_SV*100/prot_women
      prot_water_women_LD=Cprot_water_women_LD*100/prot_women
      prot_water_women_LL=Cprot_water_women_LL*100/prot_women
      prot_water_women_DW=Cprot_water_women_DW*100/prot_women
      prot_water_women_NC=Cprot_water_women_NC*100/prot_women
      prot_water_women_SN=Cprot_water_women_SN*100/prot_women
      prot_water_women_NO=Cprot_water_women_NO*100/prot_women
  #calculating girls water safty
  if(prot_girls ==0):
      prot_water_girls_LP=0
      prot_water_girls_SV=0
      prot_water_girls_LD=0
      prot_water_girls_LL=0
      prot_water_girls_DW=0
      prot_water_girls_NC=0
      prot_water_girls_SN=0
      prot_water_girls_NO=0
  else:
      prot_water_girls_LP=Cprot_water_girls_LP*100/prot_girls
      prot_water_girls_SV=Cprot_water_girls_SV*100/prot_girls
      prot_water_girls_LD=Cprot_water_girls_LD*100/prot_girls
      prot_water_girls_LL=Cprot_water_girls_LL*100/prot_girls
      prot_water_girls_DW=Cprot_water_girls_DW*100/prot_girls
      prot_water_girls_NC=Cprot_water_girls_NC*100/prot_girls
      prot_water_girls_SN=Cprot_water_girls_SN*100/prot_girls
      prot_water_girls_NO=Cprot_water_girls_NO*100/prot_girls
  #calculating men water safty
  if(prot_men ==0):
      prot_water_men_LP=0
      prot_water_men_SV=0
      prot_water_men_LD=0
      prot_water_men_LL=0
      prot_water_men_DW=0
      prot_water_men_NC=0
      prot_water_men_SN=0
      prot_water_men_NO=0
  else:
      prot_water_men_LP=Cprot_water_men_LP*100/prot_men
      prot_water_men_SV=Cprot_water_men_SV*100/prot_men
      prot_water_men_LD=Cprot_water_men_LD*100/prot_men
      prot_water_men_LL=Cprot_water_men_LL*100/prot_men
      prot_water_men_DW=Cprot_water_men_DW*100/prot_men
      prot_water_men_NC=Cprot_water_men_NC*100/prot_men
      prot_water_men_SN=Cprot_water_men_SN*100/prot_men
      prot_water_men_NO=Cprot_water_men_NO*100/prot_men
  #calculating boys water safty
  if(prot_boys ==0):
      prot_water_boys_LP=0
      prot_water_boys_SV=0
      prot_water_boys_LD=0
      prot_water_boys_LL=0
      prot_water_boys_DW=0
      prot_water_boys_NC=0
      prot_water_boys_SN=0
      prot_water_boys_NO=0
  else:
      prot_water_boys_LP=Cprot_water_boys_LP*100/prot_boys
      prot_water_boys_SV=Cprot_water_boys_SV*100/prot_boys
      prot_water_boys_LD=Cprot_water_boys_LD*100/prot_boys
      prot_water_boys_LL=Cprot_water_boys_LL*100/prot_boys
      prot_water_boys_DW=Cprot_water_boys_DW*100/prot_boys
      prot_water_boys_NC=Cprot_water_boys_NC*100/prot_boys
      prot_water_boys_SN=Cprot_water_boys_SN*100/prot_boys
      prot_water_boys_NO=Cprot_water_boys_NO*100/prot_boys

  #####   
  ##################calculating scoring using the averages#####################
  HS=sum(avg_hands_washed_HH)
  Hands_washed_score=HS/sample_tents# sum of all avg households hands washed wrt sample tents
  DS=sum(avg_disease_prevention_HH)
  Disease_prevention_score=DS/sample_tents
  source_drinking_score=sum(avg_source_drinking_HH)/sample_tents # sum of all avg households source drinking wrt sample tents
  #print("score",source_drinking_score)
  CLS=sum(avg_latrine_cleanliness_HH)   # sum of all avg households clean latrine wrt sample tent
  clean_latrine_score= CLS/sample_tents
  #print(clean_latrine_score)
  fun_latrine_score=sum(avg_latrine_functionality_HH)/sample_tents  # sum of all avg households fun latrine wrt sample tents
  lock_latrine_score=sum(avg_latrine_lock_HH)/sample_tents  # sum of all avg households lock latrine wrt sample tents
  light_latrine_score=sum(avg_latrine_light_HH)/sample_tents  # sum of all avg households light latrine wrt sample tents
  look_latrine_score = sum(avg_latrine_privacy_HH)/sample_tents #sum of all avg households privacy (look) wrt sample tents
  protection_san_score=protection_san_score/sample_tents  #sum of all avg households protection san wrt sample tents
  protection_water_score=protection_water_score/sample_tents  #sum of all avg households protection water wrt sample tents
  HP=sum(avg_happy_HH)
  #print("average",HP)
  happy_partner=HP/sample_tents #sum of all avg households of happy partner wrt tents
  #print("happy score",happy_partner)
  ###################calculating scores using other scores####################
  preVar = (open_defecation_score + clean_environment_score + solid_waste_score)
  Site_score= preVar/3
  Safe_water_score=(0.25*free_res_tank_score) + (0.5*free_res_HH_score) + (0.25*source_drinking_score)
  total_latrine_score=(clean_latrine_score + fun_latrine_score + lock_latrine_score + light_latrine_score + look_latrine_score)/5
  HH_score=(Safe_water_score + total_latrine_score + Hands_washed_score + Disease_prevention_score)/4
  HCMT_score=(Site_score + HH_score)/2
  #calculating Report_AI
  if Safe_water_score >0.8 and total_latrine_score >0.8 and Hands_washed_score >0.6 and Disease_prevention_score >0.7 and open_defecation_score>0 and clean_environment_score >0 and solid_waste_score >0:
     Report_AI='Yes'
  else:
     Report_AI='No'

  ################# Fill in the values after calculations ########################
  feature.attributes["open_defecation_score"]=open_defecation_score
  feature.attributes["clean_environment_score"]=clean_environment_score
  feature.attributes["free_res_tank_score"]=free_res_tank_score
  feature.attributes["free_res_HH_score"]=free_res_HH_score
  feature.attributes["solid_waste_score"]=solid_waste_score
  feature.attributes["Hands_washed_score"]=Hands_washed_score
  feature.attributes["Disease_prevention_score"]=Disease_prevention_score
  feature.attributes["source_drinking_score"]=source_drinking_score
  feature.attributes["clean_latrine_score"]=clean_latrine_score
  feature.attributes["fun_latrine_score"]=fun_latrine_score
  feature.attributes["lock_latrine_score"]=lock_latrine_score
  feature.attributes["light_latrine_score"]=light_latrine_score
  feature.attributes["look_latrine_score"]=look_latrine_score
  feature.attributes["protection_san_score"]=protection_san_score
  feature.attributes["protection_water_score"]=protection_water_score
  feature.attributes["happy_partner"]= happy_partner
  feature.attributes["partner_knowledge"]=partner_knowledge
  ###Final scores ###
  feature.attributes["Site_score"]=Site_score
  feature.attributes["Safe_water_score"]=Safe_water_score
  feature.attributes["total_latrine_score"]=total_latrine_score
  feature.attributes["HH_score"]=HH_score
  feature.attributes["HCMT_score"]=HCMT_score
  feature.attributes["Report_AI"]=Report_AI
  #prot sani women
  feature.attributes["prot_women"]=prot_women
  feature.attributes["prot_sani_women_LP"]=prot_sani_women_LP
  feature.attributes["prot_sani_women_SV"]=prot_sani_women_SV
  feature.attributes["prot_sani_women_LD"]=prot_sani_women_LD
  feature.attributes["prot_sani_women_LL"]=prot_sani_women_LL
  feature.attributes["prot_sani_women_DW"]=prot_sani_women_DW
  feature.attributes["prot_sani_women_NC"]=prot_sani_women_NC
  feature.attributes["prot_sani_women_SN"]=prot_sani_women_SN
  feature.attributes["prot_sani_women_NO"]=prot_sani_women_NO
  #prot sani girls
  feature.attributes["prot_girls"]=prot_girls
  feature.attributes["prot_sani_girls_LP"]=prot_sani_girls_LP
  feature.attributes["prot_sani_girls_SV"]=prot_sani_girls_SV
  feature.attributes["prot_sani_girls_LD"]=prot_sani_girls_LD
  feature.attributes["prot_sani_girls_LL"]=prot_sani_girls_LL
  feature.attributes["prot_sani_girls_DW"]=prot_sani_girls_DW
  feature.attributes["prot_sani_girls_NC"]=prot_sani_girls_NC
  feature.attributes["prot_sani_girls_SN"]=prot_sani_girls_SN
  feature.attributes["prot_sani_girls_NO"]=prot_sani_girls_NO
  #prot sani men
  feature.attributes["prot_men"]=prot_men
  feature.attributes["prot_sani_men_LP"]=prot_sani_men_LP
  feature.attributes["prot_sani_men_SV"]=prot_sani_men_SV
  feature.attributes["prot_sani_men_LD"]=prot_sani_men_LD
  feature.attributes["prot_sani_men_LL"]=prot_sani_men_LL
  feature.attributes["prot_sani_men_DW"]=prot_sani_men_DW
  feature.attributes["prot_sani_men_NC"]=prot_sani_men_NC
  feature.attributes["prot_sani_men_SN"]=prot_sani_men_SN
  feature.attributes["prot_sani_men_NO"]=prot_sani_men_NO
  #prot sani boys
  feature.attributes["prot_boys"]=prot_boys
  feature.attributes["prot_sani_boys_LP"]=prot_sani_boys_LP
  feature.attributes["prot_sani_boys_SV"]=prot_sani_boys_SV
  feature.attributes["prot_sani_boys_LD"]=prot_sani_boys_LD
  feature.attributes["prot_sani_boys_LL"]=prot_sani_boys_LL
  feature.attributes["prot_sani_boys_DW"]=prot_sani_boys_DW
  feature.attributes["prot_sani_boys_NC"]=prot_sani_boys_NC
  feature.attributes["prot_sani_boys_SN"]=prot_sani_boys_SN
  feature.attributes["prot_sani_boys_NO"]=prot_sani_boys_NO
  #prot water women
  feature.attributes["prot_water_women_LP"]=prot_water_women_LP
  feature.attributes["prot_water_women_SV"]=prot_water_women_SV
  feature.attributes["prot_water_women_LD"]=prot_water_women_LD
  feature.attributes["prot_water_women_LL"]=prot_water_women_LL
  feature.attributes["prot_water_women_DW"]=prot_water_women_DW
  feature.attributes["prot_water_women_NC"]=prot_water_women_NC
  feature.attributes["prot_water_women_SN"]=prot_water_women_SN
  feature.attributes["prot_water_women_NO"]=prot_water_women_NO
  #prot water girls
  feature.attributes["prot_water_girls_LP"]=prot_water_girls_LP
  feature.attributes["prot_water_girls_SV"]=prot_water_girls_SV
  feature.attributes["prot_water_girls_LD"]=prot_water_girls_LD
  feature.attributes["prot_water_girls_LL"]=prot_water_girls_LL
  feature.attributes["prot_water_girls_DW"]=prot_water_girls_DW
  feature.attributes["prot_water_girls_NC"]=prot_water_girls_NC
  feature.attributes["prot_water_girls_SN"]=prot_water_girls_SN
  feature.attributes["prot_water_girls_NO"]=prot_water_girls_NO
  #prot water men
  feature.attributes["prot_water_men_LP"]=prot_water_men_LP
  feature.attributes["prot_water_men_SV"]=prot_water_men_SV
  feature.attributes["prot_water_men_LD"]=prot_water_men_LD
  feature.attributes["prot_water_men_LL"]=prot_water_men_LL
  feature.attributes["prot_water_men_DW"]=prot_water_men_DW
  feature.attributes["prot_water_men_NC"]=prot_water_men_NC
  feature.attributes["prot_water_men_SN"]=prot_water_men_SN
  feature.attributes["prot_water_men_NO"]=prot_water_men_NO
  #prot water boys
  feature.attributes["prot_water_boys_LP"]=prot_water_boys_LP
  feature.attributes["prot_water_boys_SV"]=prot_water_boys_SV
  feature.attributes["prot_water_boys_LD"]=prot_water_boys_LD
  feature.attributes["prot_water_boys_LL"]=prot_water_boys_LL
  feature.attributes["prot_water_boys_DW"]=prot_water_boys_DW
  feature.attributes["prot_water_boys_NC"]=prot_water_boys_NC
  feature.attributes["prot_water_boys_SN"]=prot_water_boys_SN
  feature.attributes["prot_water_boys_NO"]=prot_water_boys_NO
  FeaturesToUpdate.append(feature)
  #print("Next row ")
  #print("--------------------------------------------------------------------")
update_result = neededLayer.edit_features(updates=FeaturesToUpdate)
print("Done")
