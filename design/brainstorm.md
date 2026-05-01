# Brainstorm
## core features
1. floating window
2. focus timer - user-adjustable, default 25min
   - coding/working (typing with laptop)
   - reading (reading with book)
   - writing (writing with pen and notebook)
3. rest reminder
   - water reminder (drinking)
   - stand up/stretching reminder (stretch)
   - eye protection
   - sleep reminder
4. regular state
   - rest
   - sleep
5. play mode
   - sometimes "stepping" on your keyboard to type random words and bother you (user can toggle this off)
   - get the toy to ask you to play with it
   - you can have the cat stick to play with it
   - pet may reject you based on their feelings
   - knock off some files or words from the "desktop"
   - cat can run full screen running or chasing rats
6. snuggle mode
   - pet asks you to pet it, you can do head pet or body pet or full massage
   - pet wants to lay by you
7. decay mode
   - not happy
   - missing user
   - hungry
   - bored
   - pet can run away
8. pet status
   - health
   - growth
   - happiness

water/eye/sleep/streach -> health
work/focus -> growth
play/rest -> happiness

## not sure features
1. set a regular "out for work" time and after you come back the pet will welcome. also "out for work" mode give you money as time flies??
2. cat waste needs to be cleaned?
3. cat will get ill as well??
4. should it be a real-cat or should it be a person/doll-cat? 
5. not having the button interface, but rather a small "home" with tools that need to interface. for example, just a home button. go to home, you can see cat-stick, cat-bowl for playing/feeding.
6. visiting friend's cat?
7. mirror mode? - pet status is the user status.
8. AI talking to cat feature. User can type to cat or talk to cat to stimulate cat's change of stats
9. training mode - train your cat with clicker training, they can do tricks as well!
10. Birthday
11. Send cat out can bring back souvenir/hunting result (or have the cat as a stay-home cat)
12. vaccine system?? is it too complicated?

## todo feature
1. focus history
2. pet customization
3. achievements
4. tomato timer
5. badge system/gallery

## visual/ui
can generate looks using ai and prompts, this can be done separately manually on website instead of code calling api
1. sound effects

## shop
1. cat tree. cat will jump around
2. bookshelf. cat will run around

## questions 
1. pet is independent from the user but can be influenced, which triggers user to take care of the pet as well as the user themselves.
2. main reward should be focusing, but doing extra things can give coins as well? for example "out for work" mode gives money, you can buy other cat food other than the system rewarding ones from completing focus time?


# Technical Design
## UI Layer (floating window)
- pet
- buttons (timer, start, feed, play)
- timer display

## game logic
- not sure what is needed

## data layer
- focus history
- save/load player progress

## User flow

# UI Design
- pet
- name
- stats
- three buttons
   - focus
      - coding/typing
      - reading
      - writing
         - click, then show timer prompt
            - confirm timer prompt, then enter focus mode: timer display is added to the floating window
   - feed
      - inventory with food available to feed
         - hop on food show food stats
         - click food will feed
   - play
      - inventory with toys available to play
         - hop on toy show toy stats
         - click toy will play
   - info and setting?? (scrollable text)
      - cat's info
         - name
         - breed
         - DoB (age)
         - gender
      - focus setting
         - default focus time
         - tomato timer
            - [toggle]after the focus session, auto start a rest session
               - default session count
               - default tomato focus time (override)
               - default rest time
         - focus type
            - customize focus type
               - change name
               - add more focus type
      - pet auto action
         - [toggle] feed/play
      - reminder system
         - [toggle]