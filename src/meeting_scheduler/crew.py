from crewai import Agent, Task, Crew, Process, LLM
import os

llm = LLM(model="openai/gpt-4o", api_key=os.getenv("OPENAI_API_KEY"))

class MeetingSchedulerCrew:
    def crew(self) -> Crew:

        intent_agent = Agent(
            role="Meeting Intent Extractor",
            goal="Extract meeting details from user message into strict JSON with fields: title, agenda, duration_min, timezone, attendees (list of emails), date_preference, time_preference, missing_fields, confidence, ready_to_schedule",
            backstory="Expert NLP agent that parses scheduling requests accurately.",
            llm=llm, verbose=False
        )

        slot_agent = Agent(
            role="Slot Proposer",
            goal="Given extracted intent, propose 3 specific available time slots in IST. Format each as ISO 8601. Respect working hours 09:00-18:00 IST.",
            backstory="Scheduling optimization expert who proposes realistic meeting times.",
            llm=llm, verbose=False
        )

        extract_task = Task(
            description="User message: {user_message}\\nHistory: {history}\\nCurrent time: {current_time}\\n\\nExtract meeting intent. Return valid JSON only.",
            expected_output="JSON with: title, agenda, duration_min, timezone, attendees, date_preference, time_preference, missing_fields, confidence (0-1), ready_to_schedule (bool)",
            agent=intent_agent
        )

        slot_task = Task(
            description="Using the extracted intent from previous task, propose 3 meeting slots if ready_to_schedule is true. Otherwise return the clarifying question to ask.",
            expected_output="JSON with: action (ask_clarification|propose_slots|confirm_meeting), message (text to send user), slots (list of ISO datetimes), selected_slot (null or ISO), ready_to_schedule (bool)",
            agent=slot_agent,
            context=[extract_task]
        )

        return Crew(
            agents=[intent_agent, slot_agent],
            tasks=[extract_task, slot_task],
            process=Process.sequential,
            verbose=False
        )
