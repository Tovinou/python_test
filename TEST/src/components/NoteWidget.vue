<template>
  <div class="note">
    <textarea
      v-model="noteText"
      @input="updateNote"
      placeholder="Write your note here..."
      class="note-textarea"
    ></textarea>
    <button @click="deleteNote" class="delete-button">Delete</button>
  </div>
</template>

<script setup lang="ts">
import { ref, watch } from 'vue'

interface Note {
  id: number
  text: string
}

const props = defineProps<{
  note: Note
}>()

const emit = defineEmits<{
  update: [note: Note]
  delete: []
}>()

const noteText = ref(props.note.text)

watch(() => props.note.text, (newText) => {
  noteText.value = newText
})

const updateNote = () => {
  emit('update', { ...props.note, text: noteText.value })
}

const deleteNote = () => {
  emit('delete')
}
</script>

<style scoped>
.note {
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 15px;
  background: white;
  display: flex;
  flex-direction: column;
}

.note-textarea {
  width: 100%;
  min-height: 150px;
  border: 1px solid #ccc;
  border-radius: 4px;
  padding: 10px;
  font-size: 14px;
  font-family: inherit;
  resize: vertical;
  margin-bottom: 10px;
}

.delete-button {
  align-self: flex-end;
  padding: 8px 16px;
  background: #dc3545;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.delete-button:hover {
  background: #c82333;
}
</style>

