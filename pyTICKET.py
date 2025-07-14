#############################################
#
## Leave Credits aka the first 15 lines
#
# File made by Butcher aka disembodied.rams
#
## Copyright © 2025 disembodied.rams
#
## Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to use, modify, and distribute the Software, subject to the following conditions:
## 1. Attribution Required - The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
## 2. Credit Retention - You may not remove, alter, or obscure any author attribution, credits, or acknowledgments included in the Software or its files. These credits must remain visible and intact in all uses and distributions.
#
# Much Love <3
#############################################


# How to use?
## Basic Bot 
############
# 1. Make a discord bot in https://discord.com/developers/applications/
# 2. Go to "Installation" Make sure both user install and guild are clicked
# 3. make sure the guild install scopes have "Bot" toggled and set the perms to "Administrator"
# 4. Copy link and invite to server
# 5. Go To "Bot" and Reset token and scroll all the way down and place it at the bottom
# 6. Go to "Ticket Code" section to fill out the rest of the code

## Discord Server
############
# 1. Make a Category named "Tickets" this is for when people make tickets it goes there
# 2. 2 choices add a channel to the "Tickets" Category or make a new Category named "Support"
# 3. Do !ticket 
# boom you have a ticket bot



# Imports
##############

import discord
from discord.ext import commands, tasks
from discord.ui import View, Select, Button
from datetime import datetime, timedelta
from discord import Embed, Interaction, SelectOption, ButtonStyle


# Discord Bot Stuff
##############

intents = discord.Intents.default()
intents.members = True  
intents.message_content = True  
intents.presences = True  
intents = discord.Intents.all()



# Ticket Code
##############

logging.basicConfig(level=logging.DEBUG)

# just right click on the role, copy role id and put them down below make sure to add ","
SUPPORT_ROLE_IDS = [Must Replace with the ID's of the support roles,]


class TicketSystem(View):
    def __init__(self):
        super().__init__(timeout=None)

        select = Select(
            placeholder="Choose a reason for your ticket",
            min_values=1,
            max_values=1,
            # you can have as many as you want just copy and paste and fill it out,
            # this is just the standard stuff
            options=[
                discord.SelectOption(label="Support", description="General support questions", emoji="🛠️"),
                discord.SelectOption(label="Report", description="Report an issue or a Person", emoji="⚠️"),
            ]
        )
        select.callback = self.select_callback
        self.add_item(select)

    async def select_callback(self, interaction: Interaction):
        reason = interaction.data['values'][0]
        user = interaction.user
        guild = interaction.guild
        ticket_name = f"ticket-{reason.lower()}-{user.name}".replace(" ", "-").lower()

        category = discord.utils.get(guild.categories, name="Tickets")
        if not category:
            category = await guild.create_category("Tickets")

        ticket_channel = await guild.create_text_channel(ticket_name, category=category)

        await ticket_channel.set_permissions(guild.default_role, read_messages=False)
        await ticket_channel.set_permissions(user, read_messages=True, send_messages=True)
        for role_id in SUPPORT_ROLE_IDS:
            role = guild.get_role(role_id)
            if role:
                await ticket_channel.set_permissions(role, read_messages=True, send_messages=True)

        embed = Embed(
            title=f"New Ticket - {reason}",
            description=f"{user.mention}, please describe your issue.\nA team member will assist you shortly.",
            color=discord.Color.blue()
        )
        embed.set_footer(text="Use the buttons below to manage the ticket.")

        view = TicketButtons(user.id)
        await ticket_channel.send(embed=embed, view=view)

        await interaction.response.send_message(
            f"✅ Your ticket for **{reason}** has been created: {ticket_channel.mention}",
            ephemeral=True
        )


# Claim and Close ticket when ones open
##############

class TicketButtons(View):
    def __init__(self, opener_id):
        super().__init__(timeout=None)
        self.opener_id = opener_id

    @discord.ui.button(label="Claim Ticket", style=ButtonStyle.green, custom_id="claim_ticket")
    async def claim(self, interaction: Interaction, button: Button):
        if interaction.user.id == self.opener_id:
            await interaction.response.send_message("You can't claim your own ticket.", ephemeral=True)
            return

        if not any(role.id in SUPPORT_ROLE_IDS for role in interaction.user.roles):
            await interaction.response.send_message("You don't have permission to claim this ticket.", ephemeral=True)
            return

        button.disabled = True
        button.label = f"Claimed by {interaction.user.name}"
        button.style = ButtonStyle.gray
        await interaction.message.edit(view=self)

        await interaction.response.send_message(f"{interaction.user.mention} has claimed this ticket.", ephemeral=False)

    @discord.ui.button(label="Close Ticket", style=ButtonStyle.red, custom_id="close_ticket")
    async def close(self, interaction: Interaction, button: Button):
        await interaction.response.send_message("Closing this ticket...", ephemeral=True)
        await interaction.channel.delete()


# Create a ticket
##############

@bot.command()
async def ticket(ctx):
    view = TicketSystem()
    embed = Embed(
        title="Create a Ticket",
        description="Please select a reason for your ticket from the dropdown below:",
        color=discord.Color.green()
    )
    embed.set_footer(text="We will assist you as soon as possible!")
    await ctx.send(embed=embed, view=view)
    
    
# Bot Token MUST REPLACE
##############

bot.run("Token Goes Here!")
