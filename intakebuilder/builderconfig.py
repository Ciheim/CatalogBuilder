#what kind of directory structure to expect? 
#For a directory structure like /archive/am5/am5/am5f3b1r0/c96L65_am5f3b1r0_pdclim1850F/gfdl.ncrc5-deploy-prod-openmp/pp
# the output_path_template is set as follows.
#We have NA in those values that do not match up with any of the expected headerlist (CSV columns), otherwise we
#simply specify the associated header name in the appropriate place. E.g. The third directory in the PP path example
#above is the model (source_id), so the third list value in output_path_template is set to 'source_id'. We make sure
#this is a valid value in headerlist as well.
#The fourth directory is am5f3b1r0 which does not map to an existing header value. So we simply NA in output_path_template
#for the fourth value.

#catalog headers
#The headerlist is expected column names in your catalog/csv file. This is usually determined by the users in conjuction
#with the ESM collection specification standards and the appropriate workflows.

headerlist = ["activity_id", "institution_id", "source_id", "experiment_id",
                  "frequency", "modeling_realm", "table_id",
                  "member_id", "grid_label", "variable_id",
                  "temporal_subset", "chunk_freq","grid_label","platform","dimensions","cell_methods","path"]

#what kind of directory structure to expect?
#For a directory structure like /archive/am5/am5/am5f3b1r0/c96L65_am5f3b1r0_pdclim1850F/gfdl.ncrc5-deploy-prod-openmp/pp
# the output_path_template is set as follows.
#We have NA in those values that do not match up with any of the expected headerlist (CSV columns), otherwise we
#simply specify the associated header name in the appropriate place. E.g. The third directory in the PP path example
#above is the model (source_id), so the third list value in output_path_template is set to 'source_id'. We make sure
#this is a valid value in headerlist as well.
#The fourth directory is am5f3b1r0 which does not map to an existing header value. So we simply NA in output_path_template
#for the fourth value.

output_path_template = ['NA','NA','source_id','NA','experiment_id','platform','custom_pp','modeling_realm','cell_methods','frequency','chunk_freq']

output_file_template = ['modeling_realm','temporal_subset','variable_id']

#OUTPUT FILE INFO is currently passed as command-line argument.
#We will revisit adding a csvfile, jsonfile and logfile configuration to the builder configuration file in the future.
#csvfile =  #jsonfile =  #logfile =

#######################################################
######### ADDITIONAL SEARCH FILTERS ###########################

dictFilter = {}
dictFilterIgnore = {}
dictFilter["modeling_realm"]= 'atmos_cmip'
dictFilter["frequency"] = "monthly"
dictFilter["chunk_freq"] = "5yr"
dictFilterIgnore["remove"]= 'DO_NOT_USE'
