# arknights-macro
Does laundry (and recruit too)

Macro Recorder demands 200+ evergreens a year for a handful of variables, so I'm ditching it. God bless ChatGPT.
## Requirements
- Windows PowerToys (text extractor, win+shift+t)
- OBS (to track progress and errors in execution, not necessary)

I'm running 2 tc, 4 fac, 3 pp.

Recruitment should ignore slots with 'Top Operator', 'Senior Operator' and 'Robot' tags.
## DIY
- Set up your own base work team in 'game\base\work_2traders.py' (I switch back and forth between 1 and 2 tc over time). There is no convenient way to filter operators in game by name, so good luck with that. I had to create quite a workaround to get Siege in trade post.
- Make your own script for farming in 'game\farm\\' and add it to '1_start.py' (don't remember exactly why I made 0_start and 1_start separate, whatever).
- I set the whole thing up to wake up PC using some kind of wake script, I tried to implement it using Python but it didn't work and I don't want to fix it so I used Macro Recorder again. Just set it up with Windows Task Scheduler, it should work. Execution of 0_start bat files is dependant on schedule:
  - '0_start_work_out.bat' a normal run, will clear the whole base of workers, except office, where I have Whisperain with filled refreshes so she doesnt need to rest (might change it later as I didn't have enough rest room for her in previous iterations and I have now). In order to make things consistent I decided in the end not to add second shift and just keep the base empty while the rest in ongoing. It reduces productivity by ~20% but adding them makes this a giant headache to set up. Especially if you happen to get a new operator, you need to redo the thing anyway, but with two shifts it becomes almost impossible to do so conveniently.
  - '0_start_rest.bat' 6 hours later it opens the game, adds new op's to rest and closes.
  - '0_start_work_in.bat' a normal run, 6 more hours later it will clear dormitories, add workers and fill dormitories with placeholders (for Rosmontis)
  - '0_start_work.bat' every 12 hours would just let it run and collect resources. With Mlynar and 3 smileys, I use a 2.5 day loop (4 smileys can give 3 day loop), so work_out --6 hours--> rest --6 hours--> work_in --12 hours--> work --12 hours--> work --12 hours--> work --12 hours--> work_out again
- Something else I didn't see coming because I'm not a god coder. God bless ChatGPT.
## To Do
- Somehow make PowerToys more consistent and code it to search for operators when filling work. That would bypass the need to be precise with operator picking, allow to make second shift and ignore more operators joining roster and messing up macro spacing.
- Merge 0_start and 1_start.
- Make the whole thing more modular, so one doesn't have to code from scratch to do anything.
