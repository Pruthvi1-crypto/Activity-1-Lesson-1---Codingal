#part1 :ask teh agent for their details

name=input("Please enter your name: ")

gadget=input("Please enter your favorite gadget: ")

# part2: Store teh agent deatils using different data types

agent_number=7

speed_rating=9.5

mission_count=12

height_m=1.65

is_active=True

# part3 :print easch details along with its data tyep

print("Name is:",name, "type:",type(name))

print("Gadget is:",gadget, "type:",type(gadget))

print("Agent number is:",agent_number, "type:",type(agent_number))

print("Speed rating is:",speed_rating, "type:",type(speed_rating))

print("Mission count is:",mission_count, "type:",type(mission_count))

print("Height in meters is:",height_m, "type:",type(height_m))

print("Is active is:",is_active, "type:",type(is_active))

# part 4: typecast tehnumbers and tru/false value into text

name_text=str(name)

gadget_text=int(gadget)

agent_number_text=str(agent_number)

speed_rating_text=str(speed_rating)

mission_count_text=str(mission_count)

height_m_text=str(height_m)

is_active_text=str(is_active)

print("Name is:",name_text, "type:",type(name_text))

print("Gadget is:",gadget_text, "type:",type(gadget_text))

print("Agent number is:",agent_number_text, "type:",type(agent_number_text))

print("Speed rating is:",speed_rating_text, "type:",type(speed_rating_text))

print("Mission count is:",mission_count_text, "type:",type(mission_count_text))

print("Height in meters is:",height_m_text, "type:",type(height_m_text))

print("Is active is:",is_active_text, "type:",type(is_active_text))

# part5: slice

b=name_text[0:3]#[start:end]

print(b)

# negative index

a=name_text[-1:]

print(a)

# part 6: reverse the string

c=name_text[::-1]

print(c)

# part7 : join everything together to buid the final message

message="Hello " + name_text.upper() + ", how are you? "

print(message)