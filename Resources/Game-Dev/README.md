# Unreal Engine 5 Mentorship

## Weekly Assignments & Final Project Compilation

> **Submission Policy (applies to every assignment):** Upload a 30–60 second screen recording showing the level**
overview and the player completing the level, unless a specific week states otherwise. The recording must be raw,
unedited gameplay — no AI-generated footage, no edits, and no clips taken from social media. Upload the video to
Google Drive and share the link in the `#submissions` channel.

## Week 1 – Game Dev Fundamentals (Unity / Unreal / Godot)
Attention Mentees: This is the first weekly assignment. Create a new Third Person Project in Unreal Engine
5 and design a simple obstacle course level. Assignments are curated for your own benefit, so complete the
level and record it yourself.
### Requirements
- Use the Third Person Template
- Create a level named FirstLevel
- Create 1 floor
- Add at least 5 platforms
- Add at least 2 ramps
- Add at least 3 obstacles
- Make sure the player can start from a Player Start and reach the finish area
- Test the level and fix any issues
### Bonus Challenge
- Rotating cube, or
- Moving platform, or
- Launch pad

## Week 2 – C# / C++ for Games
Build on your obstacle course by adding simple interactivity. Use the Third Person template (Blueprint) again
and create a new level called SecondLevel. The goal is to introduce Blueprint-driven behaviors and triggers
— for example, a Trigger Box that fires an event (such as a door opening or a platform moving) when the
player overlaps it, using an OnComponentBeginOverlap event. Think of a simple mechanic such as a
pressure plate that opens a gate. Also expand your level's layout so the player must navigate vertically as
well as horizontally, and use Modeling Mode (Shift+5) to block out geometry quickly.
### Requirements

- Use the Third Person template (Blueprints) for your UE5 project
- Create a new map named SecondLevel
- Build at least two connected areas (e.g. two floors or sections connected by ramps or stairs)
- Add at least 3 static objects or obstacles (platforms, walls, crates, etc.)
- Use Modeling Mode (Shift + 5) to quickly block out your geometry
- Add at least one Blueprint-driven interactive element: place a Trigger Box, add an
OnComponentBeginOverlap event, and make it perform an action (opening a door, starting a moving
platform, launching the player, or another mechanic)
- Ensure a Player Start is placed and the player can travel from the start to a clear finish area
- Thoroughly test the level: adjust collisions where necessary, ensure overlap events fire correctly, and make
sure the level is fully playable start to finish
### Bonus Challenge
- Add a rotating hazard
- Create a moving elevator
- Add a timed switch
- Create a collectible item with a score system
### Submission
- A quick overview of the level
- The player completing the level
### Resources
Unreal Engine Blueprints Playlist: https://www.youtube.com/playlist?list=PLZlv_N0_O1gZTBUZfQy0Am9ucvXpOV6Ii

## Week 3 – Game Design Principles
Continue using the Third Person (Blueprint) template and create a new level named ThirdLevel. Build a
small playable level where the player collects items while navigating obstacles, add a checkpoint system so
the player respawns at the latest checkpoint instead of the start after falling, and display the number of
collected items using a basic UMG widget. Create reusable Blueprint Actors for collectibles and checkpoints
rather than placing individual meshes.
### Requirements
- Use the Third Person template (Blueprints)
- Create a new map named ThirdLevel
- Build a level with multiple platforms/areas connected using jumps, ramps, or stairs
- Add at least 5 collectible items (coins, gems, cubes, or any mesh) via a reusable Blueprint Actor
- When the player overlaps a collectible: destroy/hide it and increase the player's score/count
- Display the current collectible count using a UMG Widget Blueprint
- Add at least one checkpoint using a Blueprint Actor; overlapping it updates the respawn location

- If the player falls off the map, they should respawn at the latest checkpoint instead of the Player Start
- Add a clear Finish Area reached after collecting all required items
- Thoroughly test: collectibles should not be collected twice, UI should update correctly, checkpoints should
work reliably, and the player should always be able to complete the level
### Bonus Challenge
- Create a locked door that opens only after collecting all items
- Add a countdown timer
- Add rotating or moving hazards
- Create a simple health system
- Add particle effects or sounds when collecting items
- Display a “Level Complete!” screen when the player finishes
### Submission
- A quick overview of the level
- Collecting multiple items
- Activating a checkpoint
- Falling (or demonstrating the respawn system)
- Completing the level
### Resources
Unreal Engine Blueprints Playlist: https://www.youtube.com/playlist?list=PLZlv_N0_O1gZTBUZfQy0Am9ucvXpOV6Ii

## Week 4 –  Publishing & Portfolio
Continue using the Third Person (Blueprint) template and create a new level named FourthLevel. Build a
small playable level where the player must reach the finish area while avoiding enemy AI, using AI
Controllers, Nav Mesh, and Pawn Sensing / AI Perception. Treat the level as a stealth or survival challenge
where the player must avoid being caught while navigating through the level.
### Requirements
- Use the Third Person template (Blueprints)
- Create a new map named FourthLevel
- Build a level with multiple paths or rooms
- Add a Nav Mesh Bounds Volume covering the playable area
- Create an Enemy Blueprint using a Character, and an AI Controller Blueprint for the enemy
- Make the enemy patrol between at least 3 patrol points
- Detect the player using Pawn Sensing or AI Perception
- When the player is detected, the enemy should chase them; if the player escapes, the enemy should return
to patrolling
- If the enemy touches the player, respawn the player at the latest checkpoint (or Player Start)

- Thoroughly test: AI should patrol smoothly, detection should work reliably, the enemy should chase only
after detecting the player and return to patrol after losing sight of them, and the player should still be able to
complete the level
### Bonus Challenge
- Add multiple enemies with different patrol routes
- Display a “Detected!” warning on the screen
- Add a flashlight or vision cone for the enemy
- Make the enemy walk and run at different speeds
- Play sounds when the player is detected
- Add a hiding spot where the AI loses sight of the player
### Submission
- A quick overview of the level
- The enemy patrolling
- The enemy detecting and chasing the player
- Escaping from the enemy
- Respawning after getting caught
- Completing the level
### Resources
Unreal Engine Blueprints Playlist: https://www.youtube.com/playlist?list=PLZlv_N0_O1gZTBUZfQy0Am9ucvXpOV6Ii
Enemy AI Playlist: https://youtube.com/playlist?list=PLNwKK6OwH7eW1n49TW6-FmiZhqRn97cRy

## Week 5 – Combat System & Enemy Elimination
Continue using the Third Person (Blueprint) template and create a new level named FifthLevel. Build a small
playable level where the player must defeat enemies before reaching the finish area, implementing a basic
attack system, enemy health, damage handling, and a victory condition. Treat the level as a small dungeon or
arena where enemies guard the exit.
### Requirements
- Use the Third Person template (Blueprints)
- Create a new map named FifthLevel
- Build a level with multiple rooms or combat areas
- Add at least 3 Enemy AI (you may reuse the enemy from Week 4), each with a Health variable (e.g. 100 HP)
- Create a simple player attack: melee, line trace, sphere trace, or projectile
- When the player's attack hits an enemy, reduce its health (a hit effect or sound is recommended)
- When an enemy's health reaches zero, destroy it and increase the player's kill count
- Display the current kill count using a UMG Widget Blueprint
- Add a Finish Area that only becomes accessible after all enemies have been defeated

- Thoroughly test: attacks should register consistently, enemies should only die after enough damage, kill
count should update correctly, the finish area should unlock only after all enemies are defeated, and the
player should always be able to complete the level
### Bonus Challenge
- Add attack cooldowns
- Add enemy attack animations
- Add player health and health pickups
- Add floating damage numbers
- Add a boss enemy with higher health
- Play a death animation before destroying enemies
- Create multiple enemy types with different health or movement speeds
### Submission
- A quick overview of the level
- The player fighting multiple enemies
- Defeating all enemies
- The kill counter updating
- The exit unlocking
- Completing the level
### Resources
Unreal Engine Blueprints Playlist: https://www.youtube.com/playlist?list=PLZlv_N0_O1gZTBUZfQy0Am9ucvXpOV6Ii
Enemy AI Playlist: https://youtube.com/playlist?list=PLNwKK6OwH7eW1n49TW6-FmiZhqRn97cRy

## Final Assignment – Build Your Own Mini Game
Continue using the Third Person (Blueprint) template and create a new level named FinalLevel. Build a 5–10
minute playable game that combines everything covered throughout the mentorship. Be creative with your
theme — adventure, dungeon crawler, survival, sci-fi mission, horror, fantasy quest, or anything else.
### World Design
- Create a level with multiple areas or rooms
- Include clear progression from start to finish
- Use proper lighting and environment assets
### Inventory & Items
- Create an inventory system
- Allow the player to pick up items
- Implement at least one usable item (Key, Potion, etc.)
- Display the inventory using a UMG Widget
- Use inventory items to unlock progression
### NPC & Dialogue
- Add at least one NPC
- Implement a dialogue system using UMG
- NPC should provide instructions, story, or a quest
### Objective / Quest System
- Display the current objective on screen
- Update objectives as the player progresses
- Complete objectives in sequence
### Enemy AI & Combat
- Include multiple enemies
- Enemies should patrol, detect, chase, and attack the player
- Implement player attacks
- Enemies should have health and die correctly
- Include at least two enemy types with different behaviour or stats
### Boss Fight
- Add a boss enemy with significantly more health
- Boss should use at least two different attacks or attack patterns
- Display a Boss Health Bar using UMG
- Defeating the boss should unlock the ending

### Player Systems
- Player Health
- Health pickups
- Attack cooldown
- Kill counter
### Save & Checkpoints
- Add at least one checkpoint
- Player should respawn from the latest checkpoint after dying
- Save player progress using a SaveGame Blueprint
### UI
- Health Bar
- Inventory
- Kill Counter
- Objective Display
- Boss Health Bar
- Victory / Game Over screen
### Cinematics
- Create an intro cutscene using a Level Sequence
- Create an ending cutscene after completing the game
- Disable player input during cinematics
### Polish
- Sound effects
- Background music
- Particle effects
- Hit effects
- Death effects
- Basic menu (Pause Menu or Main Menu)
### Bonus Challenge
- Multiple quests
- Multiple NPCs
- Secret area or hidden collectibles
- Ranged enemies
- Multiple boss phases
- Dynamic music
- Puzzle section
- Achievement or scoring system

- Settings menu
- Save slots
- Minimap
### Submission
Record a 2–5 minute screen recording (not the usual 30–60 seconds) showing:
- Level overview
- Dialogue with NPC
- Inventory system
- Objectives updating
- Combat with enemies
- Boss fight
- Save/Checkpoint system
- UI elements
- Intro and ending cutscenes
- Completing the game
Upload the video to Google Drive and post the link in the #submissions channel. You may also upload your
Unreal Engine project or a packaged Windows build if you'd like to showcase your work. As always, the video
must be raw gameplay — no edits, AI-generated content, or clips taken from social media.
### Resources
Unreal Engine Blueprints Playlist: https://www.youtube.com/playlist?list=PLZlv_N0_O1gZTBUZfQy0Am9ucvXpOV6Ii
You're encouraged to explore Unreal Engine documentation and other learning resources to implement
features beyond what was covered during the mentorship. Good luck, and have fun building your first
complete game!
