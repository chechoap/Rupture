import DialogueHandler
import NPCs

__author__ = "Lapse"

dh = DialogueHandler
#dh.introtext()

dh.choices()

npc = NPCs
Human207 = npc.Human("Carlos", 0, 0, 0)
print(Human207.times_talked_to)