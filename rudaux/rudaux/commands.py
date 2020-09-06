import os
import rudaux

# this is the only command that gets called on the student hub (for now)
# it should be called every X minutes using a cron job (X = 15, say, if you want your snapshots to have a max resolution of 15 mins)
# snapshots will only happen once per assignment (and once per override), so even if you set X = 1, it'll just make this command run a bunch without
# actually doing anything. The only cost is that it has to run this code every minute, which is probably too much. Most assignments are due
# on the hour / half hour at most, so every 15 should almost always be fine.
def submission_snapshot(args):
    course = rudaux.Course(args.directory)
    # if course setup fails, do ???
    # do a non-blocking update: 
    # if update fails (e.g. canvas is down), just take snapshots based on previous course obj. Snapshots are cheap and we may as well be conservative
    try:
        course.synchronize()
    except:
        pass
    # take snapshots of every assignment that has passed with no existing snapshot
    course.jupyterhub_snapshot()
    # send any notifications generated by this code (e.g. failed snapshots) to instructors
    course.send_notifications()


#Ideas for other commands:
#status #return a report of status; subcommands:
##assignment (graded / feedback / solutions / etc)
##snapshot schedule 
##hard drive / memory usage? 
##errors in assignment grading
#
#schedule_tasks #creates a schedule of commands that run automatically
#               #snapshots, cloning repos, pulling, etc
#
#run #force running of a particular task now
#
##same commands as dictauth, just for rudaux_config
##these will call dictauth commands
#encrypt_password
#
#graders:
#list
#add
#remove

