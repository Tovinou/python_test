<template>
  <div class="timer">
    <div class="timer-display" @click="editTime" v-if="!isEditing">
      {{ timer.time }}
    </div>
    <input
      v-else
      v-model="editValue"
      @blur="saveTime"
      @keyup.enter="saveTime"
      class="timer-input"
      ref="timeInput"
    />
    <div class="timer-controls">
      <button @click="start" v-if="!timer.isRunning">Start</button>
      <button @click="pause" v-else>Pause</button>
      <button @click="reset">Reset</button>
      <button @click="deleteTimer" class="delete-button">Delete</button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'

interface Timer {
  id: number
  time: string
  isRunning: boolean
  intervalId?: number
}

const props = defineProps<{
  timer: Timer
}>()

const emit = defineEmits<{
  update: [timer: Timer]
  delete: []
}>()

const isEditing = ref(false)
const editValue = ref('')
const timeInput = ref<HTMLInputElement | null>(null)
const intervalId = ref<number | undefined>(undefined)

const parseTime = (timeStr: string): number => {
  const [minutes, seconds] = timeStr.split(':').map(Number)
  return minutes * 60 + seconds
}

const formatTime = (totalSeconds: number): string => {
  const minutes = Math.floor(totalSeconds / 60)
  const seconds = totalSeconds % 60
  return `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`
}

const start = () => {
  if (props.timer.isRunning) return
  
  const updatedTimer = { ...props.timer, isRunning: true }
  emit('update', updatedTimer)

  intervalId.value = window.setInterval(() => {
    const currentSeconds = parseTime(props.timer.time)
    if (currentSeconds > 0) {
      const newTime = formatTime(currentSeconds - 1)
      emit('update', { ...props.timer, time: newTime })
    } else {
      pause()
    }
  }, 1000)
  
  updatedTimer.intervalId = intervalId.value
  emit('update', updatedTimer)
}

const pause = () => {
  if (intervalId.value) {
    clearInterval(intervalId.value)
    intervalId.value = undefined
  }
  emit('update', { ...props.timer, isRunning: false, intervalId: undefined })
}

const reset = () => {
  pause()
  emit('update', { ...props.timer, time: '15:00', isRunning: false })
}

const editTime = () => {
  isEditing.value = true
  editValue.value = props.timer.time
  setTimeout(() => {
    timeInput.value?.focus()
    timeInput.value?.select()
  }, 0)
}

const saveTime = () => {
  const timeRegex = /^(\d{1,2}):(\d{2})$/
  if (timeRegex.test(editValue.value)) {
    const [minutes, seconds] = editValue.value.split(':').map(Number)
    if (minutes < 100 && seconds < 60) {
      emit('update', { ...props.timer, time: editValue.value })
    }
  }
  isEditing.value = false
}

const deleteTimer = () => {
  pause()
  emit('delete')
}

onUnmounted(() => {
  if (intervalId.value) {
    clearInterval(intervalId.value)
  }
})
</script>

<style scoped>
.timer {
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 20px;
  background: white;
}

.timer-display {
  font-size: 48px;
  text-align: center;
  margin-bottom: 15px;
  cursor: pointer;
  font-weight: bold;
}

.timer-input {
  font-size: 48px;
  text-align: center;
  width: 100%;
  border: 2px solid #007bff;
  border-radius: 4px;
  padding: 10px;
  margin-bottom: 15px;
}

.timer-controls {
  display: flex;
  gap: 10px;
  justify-content: center;
}

.timer-controls button {
  padding: 8px 16px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  background: #007bff;
  color: white;
}

.timer-controls button:hover {
  background: #0056b3;
}

.delete-button {
  background: #dc3545 !important;
}

.delete-button:hover {
  background: #c82333 !important;
}
</style>

