<template>
  <div id="app">
    <header>
      <h1>Timer & Notes App</h1>
      <div class="theme-selector">
        <label>Select theme: </label>
        <button 
          v-for="theme in themes" 
          :key="theme.name"
          @click="setTheme(theme.name)"
          :class="{ active: currentTheme === theme.name }"
        >
          {{ theme.name }}
        </button>
      </div>
    </header>

    <div class="controls">
      <button @click="addTimer" class="add-button">Add timer</button>
      <button @click="addNote" class="add-button">Add note</button>
    </div>

    <div class="widgets">
      <TimerWidget
        v-for="(timer, index) in timers"
        :key="timer.id"
        :timer="timer"
        @update="updateTimer"
        @delete="deleteTimer(index)"
      />
      <NoteWidget
        v-for="(note, index) in notes"
        :key="note.id"
        :note="note"
        @update="updateNote"
        @delete="deleteNote(index)"
      />
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import TimerWidget from './components/TimerWidget.vue'
import NoteWidget from './components/NoteWidget.vue'

interface Timer {
  id: number
  time: string
  isRunning: boolean
  intervalId?: number
}

interface Note {
  id: number
  text: string
}

const timers = ref<Timer[]>([])
const notes = ref<Note[]>([])
const currentTheme = ref('Light')
const themes = [
  { name: 'Light', class: 'light' },
  { name: 'Dark', class: 'dark' },
  { name: 'Forest', class: 'forest' },
  { name: 'Orange', class: 'orange' }
]

let timerIdCounter = 0
let noteIdCounter = 0

const addTimer = () => {
  timers.value.push({
    id: timerIdCounter++,
    time: '15:00',
    isRunning: false
  })
}

const addNote = () => {
  notes.value.push({
    id: noteIdCounter++,
    text: ''
  })
}

const updateTimer = (updatedTimer: Timer) => {
  const index = timers.value.findIndex(t => t.id === updatedTimer.id)
  if (index !== -1) {
    timers.value[index] = updatedTimer
  }
}

const updateNote = (updatedNote: Note) => {
  const index = notes.value.findIndex(n => n.id === updatedNote.id)
  if (index !== -1) {
    notes.value[index] = updatedNote
  }
}

const deleteTimer = (index: number) => {
  const timer = timers.value[index]
  if (timer.intervalId) {
    clearInterval(timer.intervalId)
  }
  timers.value.splice(index, 1)
}

const deleteNote = (index: number) => {
  notes.value.splice(index, 1)
}

const setTheme = (themeName: string) => {
  currentTheme.value = themeName
  const theme = themes.find(t => t.name === themeName)
  if (theme) {
    document.body.className = theme.class
    localStorage.setItem('theme', themeName)
  }
}

onMounted(() => {
  const savedTheme = localStorage.getItem('theme')
  if (savedTheme) {
    setTheme(savedTheme)
  } else {
    setTheme('Light')
  }
})
</script>

<style scoped>
#app {
  padding: 20px;
  max-width: 1200px;
  margin: 0 auto;
}

header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
  flex-wrap: wrap;
}

.theme-selector {
  display: flex;
  gap: 10px;
  align-items: center;
}

.theme-selector button {
  padding: 5px 15px;
  border: 1px solid #ccc;
  background: white;
  cursor: pointer;
  border-radius: 4px;
}

.theme-selector button.active {
  background: #007bff;
  color: white;
}

.controls {
  display: flex;
  gap: 10px;
  margin-bottom: 20px;
}

.add-button {
  padding: 10px 20px;
  background: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 16px;
}

.add-button:hover {
  background: #0056b3;
}

.widgets {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 20px;
}
</style>

