**Notice:** This script is far from perfect, and comes without any warranty. Your mileage may vary. 

## How To Setup :gear:
  
- Insert your account token(s) into the tokens.txt file. (One account ID per line, recommended 1)

- Insert any server IDs that you do not wish to leave into the exceptions.txt file. (One server ID per line)

  
#### 1・Running :zap:

- Ensure you have Python and the requests module installed. (requests should be installed by default)
- Navigate to the directory where you have downloaded/cloned the repo
- Run main.py


## Why did I make this fork? 🤔

- The original project used unescessary dependencies.
- The original project was missing the ability to exclude servers from being left.
- The original project wouldn't work very reliably due to Discord's API ratelimit. 


## Known issues 🛠️

- You may need to run the script a few times (with a few minutes apart) if you are in many servers. The Discord API seems a bit fussy about leaving lots of servers together,even with some ratelimit circumvention. 
- Some messages are inaccurate.
- This script cannot remove you from servers you own, but will report a success.

## Future Improvements 🚧

I may or may not get around to implementing these, but here are a few things that could be improve in future, in addition to the known issues listed above.

- Rework the script to use API response codes to determine whether or not the operation succeeded, rather than the "inaccurate" system currently used that only fails if the actual sending of the request experiences a problem.
- Improve the ratelimiting circumvention system.
- Identify causes of some servers taking a few passes to be removed and fix it.


## Will I provide additional support to this project? ❓

- Maybe. I'm busy and have other priorities to be working on, I am aware this fork could be better implemented, however whether or not I get the chance to fix things up a bit more isn't something I can guarantee. I will do my best to handle any issues or PRs submitted.
- My purpose for adapting this was for personal use only. 
