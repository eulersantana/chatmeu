from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot(
    'Euler',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand.',
            'maximum_similarity_threshold': 0.90
        }
    ]
)

trainer = ListTrainer(bot)
# Treino baseado no corpus em Portugues 
trainer.train("chatterbot.corpus.Portuguese")

# Treino baseado no corpus de saudações em Português
trainer.train("chatterbot.corpus.Portuguese.greetings_pt-BR")

# Train based on the english conversations corpus
# Treino baseado no corpus de conversação em Português
trainer.train("chatterbot.corpus.Portuguese.conversations_pt-BR")

while True:
    try:
        print('Voce:')
        bot_input = bot.get_response(input())
        print('Bot:')
        print(bot_input)

    except(KeyboardInterrupt, EOFError, SystemExit):
        break