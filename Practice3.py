# Tried with chatGpt, will do by myself.

# class MemoryManager:
#     def __init__(self, memory):
#         self.memory = memory
#         self.allocated_blocks = {}  # (start_index: end_index)

#     def allocate(self, size):
#         # Find a sequential block of size in memory
#         for i in range(len(self.memory) - size + 1):
#             if all(self.memory[i+j] is None for j in range(size)):
#                 start_index = i
#                 end_index = i + size - 1
#                 self.allocated_blocks[start_index] = end_index
#                 return start_index
#         raise Exception("No block big enough to allocate")

#     def release(self, pointer):
#         if pointer not in self.allocated_blocks:
#             raise Exception("Block not allocated")
        
#         del self.allocated_blocks[pointer]

#         # Merge adjacent free blocks
#         start = pointer
#         end = pointer
#         while end + 1 in self.allocated_blocks:
#             end = self.allocated_blocks[end + 1]
#             del self.allocated_blocks[start]
#             start = end

#     def write(self, pointer, value):
#         if self.memory[pointer] != None:
#             raise Exception("Pointer does not point to an allocated block")
#         self.memory[pointer] = value
#         pointer = pointer + 1
#         return pointer

#     def read(self, pointer):
#         if self.memory[pointer] != None:
#            return self.memory[pointer]
#         else:
#             raise Exception("Pointer does not point to an allocated block")
        

# # Example usage
# memory = [None] * 100  # Initialize a memory of size 100 with all blocks free

# mem_manager = MemoryManager(memory)

# # Allocate memory
# pointer = mem_manager.allocate(10)
# print("Allocated block at pointer:", pointer)

# # Write to allocated block
# pointer = mem_manager.write(pointer, "Data")
# pointer = mem_manager.write(pointer, "Data2")
# pointer = mem_manager.write(pointer, "Data3")
# pointer = mem_manager.write(pointer, "Data4")
# pointer = mem_manager.write(pointer, "Data5")
# pointer = mem_manager.write(pointer, "Data6")
# pointer = mem_manager.write(pointer, "Data7")
# pointer = mem_manager.write(pointer, "Data8")
# pointer = mem_manager.write(pointer, "Data9")
# pointer = mem_manager.write(pointer, "Data10")


# # Read from allocated block
# data = mem_manager.read(pointer)
# print("Data read from memory:", data)

# # Release memory
# mem_manager.release(pointer)
# # Allocate memory
# pointer = mem_manager.allocate(20)
# print("Allocated block at pointer:", pointer)
# # Write to allocated block
# pointer = mem_manager.write(pointer, "popaaaaaaaaa")
# print(memory)
