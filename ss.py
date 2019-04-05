# coding: utf8
import spacy
import collections
from operator import itemgetter
nlp = spacy.load('en')


def ImportentSents(texts, num):
	Main_text = texts[num]
	texts.remove(Main_text)

	ImportentSen = []
	for sent in Main_text.sents: ## Sentences in the main text
		
		Sum_high = []
		for text in texts: ## for all texts
			a = sorted(text.sents, key = lambda x : sent.similarity(x), reverse = True)

			Sum_high.append(sent.similarity(a[0])) ## Add the Highest Sim
				
		if(sum(Sum_high) / len(Sum_high) > 0.85): ## Check if the Sen is importent
			ImportentSen.append(sent) ## Add the sen
	return ImportentSen

# def Sum_of_sums(texts):
# 	best = []
# 	for idx, val in enumerate(texts):
#     	best.append(ImportentSents(texts, idx)) ## Different Main Texts


def ss(texts):
	dic = {}

	for te in texts:
		ts = texts
		ts.remove(te)

		for sent in te.sents: ## Sentences in the main text

			Sum_high = []
			for text in ts: ## for all texts
				a = sorted(text.sents, key = lambda x: sent.similarity(x), reverse = True)

				Sum_high.append(sent.similarity(a[0])) ## Add the Highest Sim

			dic[sent] = (sum(Sum_high) / len(Sum_high))

	sorted_list = sorted(dic.items(), key = lambda kv: kv[1])
	return collections.OrderedDict(sorted_list)


			


    	


texts = []
text1 = nlp(u"""We speak English but do we know where it comes from? I didn’t know until I started to study on this subject and I learned where it comes from and how it has developed.
The history of English begins a little after A.D. 600. The ancestors of the language were wandering in the forests of northern Europe. Their language was a part of Germanic branch of Indo-European Family.
The people talking this language spread to the northern coast of Europe in the time of Roman Empire. Among this people the tribes called Angels, Saxons, Jutes which is called Anglo-Saxons come to England. The first Latin effect was in that period. Latin affected the language with the merchants traveling the tribes. Some of the words taken from Latin are; kettle, wine, cheese, butter, cheap.
Also in the 14th century Rome Empire weakened because Goths attacked to Mediterranean countries of Roman Empire and Anglo-Saxons attacked to empire. On the other hand the Celtic tribes in Scotland and Wales developed. At the end in 410 the last roman emperor  left the island to Celtic and Anglo-Saxons. Celtic and Anglo-Saxons fought for 100 years and Anglo-Saxons killed all the Celtics. In 550 Anglo -Saxons established England. During Roma Empire Latin wasn’t the native language of the kingdom because people in the country were talking Celtic.
When Anglo-Saxons became Christian in 597 they learned Latin. According to the effects to English  , the history of the language divided in to three; Old English(7th century-1100), Middle English(1100-1450/1500), Modern English (1500-now). In some books Modern English is divided in to two Early modern (1500-1700) ,Late Modern (1700-now).

When England was established there were several kingdoms  and the most advanced one was Nurthumbria. It was this period that the best of the Old English literature was written, including the epic poem Beowulf.
In the 8th century  Nurthumbrian power declined , West Saxons became the leading power. The most famous king of the West Saxons was Alfred the Great. He founded and established schools, translated or caused to be translated many books from Latin in to English.
After many years of hit-and-run raids between the European kingdoms, the Norseman landed in the year of 866 and later the east coast of the island was Norseman’s. Norse language affected the English considerably. Norse wasn’t so different from English and English people could understand Norseman. There were considerable interchanges and word borrowings (sky, give, law, egg, outlaw, leg, ugly, talk). Also borrowed pronouns like they, their, them. It is supposed also that the Norseman influenced the sound structure and the grammar of English.
Old English had some sound which we don’t know have now. In grammar, Old English was much more highly inflected that Middle English because there were case endings for nouns, more person and number endings of words and a more complicated pronoun systems, various endings for adjectives. In vocabulary Old English is quiet different from Middle English. Most of the Old English words are native English which weren’t borrowed from other languages. On the other hand Old English contains borrowed words coming from Norse and Latin.
Between 1100-1200 many important changes took place in the structure of English and Old English became Middle English. The political event which affected the administration system and language was the Norman Conquest. In 1066 they crossed the Channel and they became the master of England. For the next several next years, England was ruled by the kings whose native language was French. On the other hand French couldn’t become the national language because it became the language of the court, nobility, polite society, literature. But it didn’t replace as the language of the people. English continued to be the national language but it changed too much after the conquest.
The sound system&grammar wasn’t  so effected but vocabulary was effected much. There were word related with goverment:parliment,tax, goverment,majesty; church word: religion, parson, sermon; words for food:veal, beef, mutton, peach,lemon,cream,biscuit; colors: blue, scarlet, vermilion;  household words: curtain, chair,lamp,towel,blanket; play words: dance,chess,music,leisure,conversation; literary words: story romance, poet, literary; learned words: study, logic grammar,noun,surgeon, anatomy, stomach; ordinary words for all sorts: nice,second,very,age,bucket, final,gentel, fault, flower,count,sure, move, surprise, plain. (Clark, V.P.& Eschholz, P.A. &Rose ,A.F.; 1994;622 )
Middle English was still a Germanic language but it is different from Old English in many ways. Grammar and the sound system changed a good deal. People started to rely  more on word order and structure words to express their meaning rather than the use of case system. “This can be called as a simplification but it is not exactly. Languages don’t become simpler , they merely exchange one kind of complexity for another”( (Clark, V.P.& Eschholz, P.A. &Rose ,A.F.; 1994;622 )
For us Middle English is simpler that Old English because it is closer to Modern English.


Between 1400-1600 English underwent a couple of sound changes. One change was the elimination of a vowel sound in certain unstressed positions at the end of the words. The change was important because it effected thousands of words and gave a different aspect to the whole language.
The other change is what is called the Great Vowel Shift. This was a systematic shifting of half a dozen vowels and diphthongs in stressed syllables. For example the word name had in Middle English a vowel something like that in the modern word father;…etc. The shift effected all the words in which these vowels sounds occurred. These two changes produced the basic differences  between Middle English and Modern English. But there are several other developments that effected the language. One was the invention of printing. It was introduced to England by William Caxton in 1475. After this books became cheaper and cheaper, more people learned to read and write and advanced in communication.
The period of Early Modern English was also a period of English Renaissance, which means the development of the people. New ideas increased. English language had grown  as a result of borrowing words from French ,Latin, Greek.
The greatest writer of the Early Modern English period is Shakespeare and the best known book is the King Jones version of the BIBLE. 

In order to establish the language  they develop a dictionary. The first English Dictionary was published in 1603. Another product of the 18th century  was the invention of English Grammar. As English is replaced with Latin as the language of scholarship, it was felt to control the language.
The period where English developed most in the Modern English. In that period the people speaking that language increased too much. Now, English is the greatest language  of the  world spoken natively and as a second language. What will happen in the future? It’ll continue to grow , may be it will be the universal language.""")


text2 = nlp(u""" The english language is part of the Germanic branch of the Indo-European Family of languages. These Indo-European languages originate from Old Norse and Saxon. English originated from a fusion of languages and dialects, now called Old English :

It all started when the Germanic tribes arrived in Britain and invaded the country during the 5th century AD. Before the Germanic invasions in Britain, Britain was populated by various Celtic tribes. These Celtic tribes were united by customs, religion and common speech. But the celtic tribes lacked political unity and that made them vulnerable. During the first century, Britain was conquered by Rome. When Britain finally gained independence from Rome in the year 410 AD, the Roman legions had withdrawn from Britain and this left the country vulnerable to invaders. Inhabitants from the north began attacking the inhabitants of Britain. A lot of different Germanic tribes started to migrate to Britain, but a few stood out amongst the rest, such as the Saxons, the Angles,the Jutes, the Franks and the Frisians. They came from different parts of what is nowadays northwest Germany, Denmark and the Netherlands.

The original inhabitants of Britain spoke a Celtic language. But most of the original inhabitants were driven to the west and north by the invaders. They mainly migrated to what is now Wales, Scotland and Cornwall. The Saxons called the native Britons, ‘wealas’ and wealas meant foreigner or slave, this is where the modern word Welsh came from.

The germanic tribes were constantly fighting over power. But as time passed the different germanic cultures gradually became similar to each other until they eventually stopped seeing themselves as their individual origin but collectively as either Anglo-Saxon or English. The germanic tribes already spoke similar languages that now developed into what we now call Old English. The words England and English are derived from Engla-land (“land of the Angles”) and englisc (the language the Angles spoke).

How did the english language evolve?
The history of the english language is split up into three periods that are normally called Old English (or Anglo-Saxon), Middle English and Modern English.

Old English was the first form of English.It did not look or sound like the English we know today. The native English speakers nowadays would find it very difficult to understand Old English. But still, about half of the most commonly used words in Modern English originate from Old English. Some fun words that are derived from Old english are: axode(asked), habbaÃ° (have), rihtlice (rightly), engla (angels), heofonum (heaven), swilcum (such), hu (how) and beon (be). Old English was spoken from 450 AD until around 1100 AD.

Middle English (1100-1500)

In 1066 AD William the Conqueror, the Duke of Normandy (Normandy is part of modern France), invaded and then conquered England. The Normans spoke a dialect of Old French that is known as Anglo-Norman. This became the language of the Royal Court, the ruling classes and business classes. There was a sort of linguistic class division in this period. French was the language the upper classes spoke, and English was the language the lower classes spoke. But later in 1204 AD, King John lost the province of Normandy to the King of France. Because of this, the Norman nobles of England started to take more distance from the French Normans. England became the main concern of the Norman nobles. From 1349-1350 The black death killed around one-third of the English population. Because of these deaths the labouring classes grew in social and economical importance. Along with the rise of the importance of the labouring classes English became more important compared to Anglo-Norman as well. The nobility soon used a modified English as their native tongue. By 1362, the linguistic division between the nobility and the commoners was pretty much over.

In Britain English was the dominant language again,but many French words were added to the vocabulary. This mixture of languages is called Middle English. Middle English opposed to Old English, can be read, but it would still be difficult for modern English-speaking people. The Middle English period ended around 1500 AD with the rise of Modern English.

Early Modern English (1500-1800)

There were a few major factors that influenced Middle English and helped separate Middle and Modern English.

– The first major factor was the Great Vowel Shift. This was as sudden and big change in pronunciation that began around 1400 towards the end of the Middle English period. Vowels were being pronounced shorter and shorter. Modern English shifted into something that was more understandable for modern English speaking people.

– Another major factor was that since the 16th Century the British started to get in contact with many people from all around the world.These new contacts, and the Renaissance period of Classical learning, are the reasons that many new phrases and words were added to the language. English has been constantly adopting foreign words, especially from Latin and Greek.

– The last major factor that helped with the development of Modern English was the invention of printing. In 1476, William Caxton has brought the printing press to England in. Since then books became less expensive and literature that is written in English opposed to Latin, became more common. Now everything was printed in a common language, and that brought standardization to English. Most publishing houses were located in London so the dialect of London became the printing standard. Rules were made for spelling and grammar, and the first English dictionary was published in 1604.

Late Modern English (1800-Present)

The difference between early modern English and late modern English is mainly vocabulary. Grammar, pronunciation and spelling are mostly the same as before, but late modern English has a lot more words than early modern English. There are a few explanations for the huge expansion in words. In the first place, technology and the Industrial Revolution created the need for new words so people could describe the new creations and discoveries that were made.

For this, people created many words with Latin and Greek roots. For example, words like protein,nuclear,oxygen and vaccine did not exist before, but they were made with Greek and Latin influences. Not all the new words were created from classical roots though, English words that already existed were also combined for terms like typewriter, airplane and horsepower. Secondly, at one point one-quarter of the countries on earth belonged to the British Empire, and that’s why the English lanuage took over foreign words from many different countries.The britain empire was a maritime empire so phrases that were created onboard ships were a big influence on the english language. Finally, during the last half of the 20th century the military influence on the english language was significant. Before the Great War, both Britain and the United States had small, volunteer militaries. English military slang existed, but this barely had an impact on standard English. However, during the mid-20th century, a big number of British and American men joined the military. Because the military started to play a bigger role in a lot of people’s lives, military slang had a big impact on standard English. Military terms like landing strip, camouflage, spearhead, blockbuster, roadblock and nose dive started massively entering the standard English language.

Why did the english language become so important?
When England started trading, exploring and conquering lands, it took the language with it. The rise of the British Empire is one of the main reasons why English spread across the world. The British Empire was expanding dramatically,during the 1700s. European settlers quickly outnumbered the original population and so English was established as the dominant language in most colonies. By the late 19th century the empire’s reach was truly global and the language was also becoming global. Great Britain held colonies on every continent of the world and the trade language in those areas was English,which meant that knowing English was important. (!nog beetje eigen woorden)

After the British colonization of North America, English became the dominant language in the United States and in Canada. The growing cultural and economical influence of the US and its status as a global superpower since World War II have significantly increased the language’s spread across the world. Today, American English is predominantly influential, because of the USA’s dominance in television, popular music,cinema, trade and technology (including the Internet). Most website’s on the internet are in English. Popular American movies and tv programmes which people watch all over the world are in English. People listen to American music and English is the language mostly used for business. So the world has been exposed to english in many ways and that’s why most people know the english language and would like to study it.

Right now it has been stated by experts that around one-third of the world’s population has english as their native language and even more study English as a second language. A working knowledge of English has become a necessity in a number of area’s. It is the international language of communications, science, technology, business, medicine, aviation, maritime activities and many more. Because of that over a Billion people speak English to at least a basic level. """)

text3 = nlp(u""" When we discuss about what is language? It can be defined in different aspects. A language may be related to a specific field it can be language of humanity, science and news. Human language has a dominant position than all the languages because it’s a natural language. Language is one of the major source through which the people organize their thoughts and expresses the feelings. (Adebeyo, 1995). It means that its only human language by which a man can arrange or express his thoughts in a better way. This supports the different senses of language. If the language will not be there no one will be able to express his thoughts and share his experiences with others. As a result people will not able to learn from them.

Communication is a great tool that links the people of the world and makes the world a global village. There are some evidences that prove that communication is the most important factor of the society. It is proved by media, internet among others. Ormrod (1995) suggests that language may be described as an essential form of communication. According to behaviorist, language is learned through behavior like thinking, acting and feelings.

Origin of language
The interesting facts of living and human evolution are discussed in the origin of language. If we talk about written language it leaves some traces but spoken language has no traces. At the beginning, different system of verbal language emerged from non-linguistic and proto-linguistic source of communication. Before 4 million years human beings and chimpanzees had common ancestor. So, since the last centuries human beings have not found any signs how actually language developed because verbal communication leaves no trace.

All human beings are born with the same linguistic ability, and no one has a biological ability to adapt a specific language. Any child learns the language from his social surroundings, if a child is left in a non-native context he will not be able to learn his native language and adapt the language of the society in which he is living. From this we can say that language is not an inborn ability. It is learned by the family, people living around you. Language is the only factor that discriminates the human beings from the animal.

Changing in Languages
If we talk about language changing, varieties of languages are spoken all over the world. In this part of study we will focus that when language gets in touch with other language it causes language change. When the speakers of a language use varieties of languages in a situation the language comes in contact. Traditionally language change due to contact has been described into three categories.

Borrowing

Code-Switching

Bilingualism

Borrowing.
Thomason and Kaufman (1988) describes that borrowing is the involvement of the characteristics of other language into the native language of a speaker. The language of native speaker does not change but the change occurs due to adding incorporated characteristics. Coetsem’s (1988) defines the borrowing as when the language speaker is using the language in any other context, it incorporates the features of other languages. If Urdu speaker is speaking English language the transfer of the English language into Urdu is called borrowings.

According to Bloomfield (1933), who was the first who attempted this study and classified the lexical borrowing into dialect borrowing and cultural borrowing. Dialect borrowing is where the borrowings are from the same speech and cultural borrowing is where the borrowings are from different languages. In cultural borrowing the words from the other cultures are borrowed. The word “spaghetti” is an Italian word which is used in the culture of language from where it is borrowed. Certainly, it is an essential phenomenon especially when we talk about the effect of different languages on English.

Researchers are in the view that borrowing is a different phenomenon than the other language contacts such as emergence, code-Switching, and transfer. Poplack and associates (Poplack, 1980) and (Meechan,1995) are in the opinion that the phenomenon of code-switching and borrowing vary from each other.

Code-Switching.
Code-Switching is a crucial consequence of bilingual or multilingual speaker. A person who is bilingual or multilingual selects the language according to his/her context. The language that is selected by the speaker must be comprehensible for the addressee and the participant must understand it. (Hudson 1996). In communities where the people speak more than one language, they use different languages in different situations. The language is selected according to the rules of society in which he/she is living. Languages are varied according to situation. There is the difference between the language used in home and the language that is used in other places for various purposes.

Switching refers overlapping between two or more than two languages. It is the interchanging between two languages or more than two languages. Code-switching refers to single word interference while switching refers to constant use of such language by a bilingual speaker. According to Di pietro (1982) code-switching is when the communicants converse in more than one language in the implementation of speech act. Falhis in (1982) refers that the code-switching is the interchanging of more than one language.

Another definition that is proposed by Scotton and Ury (n.d.) say that the use of different linguistic varieties in the same discourse is called code-switching. But according to Weinreich (1953) definition, the people exchange a language to other because they want to change the situation of speech. When we observe the above definitions, it is very obvious that nobody can define the code-switching terminology. We have found divergence among the sociologists and linguists because the writers admit that there is uncertainty in this term.

Types of code-switching.
Code-Switching have been classified by the scholars in diverse types. They have given different names to these types after observing the various cases. Poplack (1989) demonstrate these types as: Tag-switching, inter-sentential and intra-sentential.

Tag switching: Tag switching means to connect one language into the other language and to switch a mark of a language into the other language. It can be at word or phrase level or both.

Inter-Sentential switching: Its means the occurrence of switching outside the boundaries at clause or sentence level. This type of switching can also take place between the conversations of the speakers (Romaine, 1989; Myer-Scotton, 1993; Hoffman, 1991).

Intra-Sentential switching: This type of code switching includes the various types of switching that take place within the phrase, sentence or clause.

There are different styles of the language so we cannot say that code-switching only occurs in the speaking of bilinguals. It can also occur among the monolinguals because of the styles of the language.

Bilingualism.
Bilingualism refers to a person who can speak two different languages. In defining the term of bilingualism we have found the disagreement among linguists. Some linguists emphasizes that a person who is bilingual must have the command on two different languages. He/she should be fluent and accurate as native speaker in both languages. A bilingual person has a feature to develop the knowledge of second language and the ability to speak it.

Types of bilingualism.
Here are discussed three major types of bilinguals.

Monocultural-Co-ordinate Bilingual is type of bilingual learns the other language or second language to fulfill his requirements and to access the information related to his needs, to research the academic subject matter. He becomes bilingual but not bi-culture because he develops his language within a culture.

Bicultural-Co-ordinate Bilingual is a bilingual person learns the second language within the speech community of second language for many reasons such as studied literature of their culture, history and tourism purposes.

Bicultural-compound Bilingual is type of bilingual learns two cultures and two languages. One at home and the other of the society in which he is living. The only way to tackle with these various definitions is to know that bilingualism is an individual feature and one can learn more than one language if he is competent enough, he can get the complete mastery of two languages.

Pidgins
Pidgins are one of the major aspects of language change.

Pidgin Languages.
Pidgins languages developed from the distinguish language varieties. They are created by the efforts of different people who speak varieties of languages. We cannot say that pidgin is the native language of some person. It is learned when people get in touch with the people who speak their language in their own context.

The people who do not have the common language to exchange their ideas, pidgins develop as a source of communication between them. Holmes (2001) states that when two groups having different languages communicate with each other in such situation where a third language has dominant position, this may called pidgins. When the people from various language contexts come in contact with each other pidgins languages are needed for their survival. For the slaves, the only way to communicate with their masters and with one another was pidgin that was their master’s language.

Cultural Impact on Language
Language changes with the time and there are a lot of features that causes that change. As a person grows a lot of factors like family, region and culture can influence the language development of a person. A culture can introduce different words which gradually become part of the language. Human beings can express thoughts and communicate with each other through language. Simply the word that is uttered by a person carrying some meaning is known as language, whereas, the culture may be referred to the activities and doings of people. Every culture has its own identity. Culture includes religion, dress, art, games, music, rituals and law.

Language policy, multilingualism and language vitality in Pakistan
Pakistan is a country with multilingual speaker. Urdu is its national language and it is the mother tongue of almost 7.57 percent people of Pakistan, although it is used at a wide range in the urban areas of Pakistan. English is still official language of Pakistan as it was when British ruled in the subcontinent. There are some other major languages of Pakistan that are:

Pakistani languages

Languages

Percentage of speakers

Urdu

7.57

Pashto

15.42

Sindhi

14.10

Punjabi

44.15

Balochi

3.57

Other

4.66

Source: Census 2001: 107

English is the official language of Pakistan. It is government language, military language, language of business contracts, signs of shops, many street signs and other enterprises use English. It is the language of law also. In most of Pakistani schools, medium of instruction is English and it is taught to all Pakistani students at school level, while at university and college level medium of instruction is English. English is boasted by the media and press of Pakistan at large scale. All the major newspapers of Pakistan are published in English. A major news channel of Pakistan is Dawn news.

Status of English in Pakistan
English language performs various functions in Pakistan.

English is Politics language.

It is the medium of instruction in Pakistani schools and colleges.

It is the source of education for the people because all scientific theories are in English.

English is the language of press and media.

It is the lingua franca.

This indicates if someone has not the knowledge of English language, it is impossible for him to get a high status in society. Most of the people in Pakistan speak English just to communicate. They don’t know the standard version of English. There are some people who are given the duty to use standard version of English. Some people say that English is not their mother language even then they can understand and speak the language. Some people in Pakistan like language teachers, policy makers, broad casters, and other institutions try to follow the standard version of language but some people just goof by the communication is affected in a bad way.

Non-native Varieties of English
According to Kachru (1978) who first introduced the nativized English variety in South Asia and he calls it English of South Asian people. In Kachru’s point of view South Asia English is another linguistic phenomenon that helps in the identity of culture. He states that nativization should be considered the result of innovative trend in linguistics. These innovations are determined through the localized form of second language. After this development the new and non-native varieties of English were gradually recognized like Indian English, Sri Lankan English, Singaporean English, Nigerian English and Pakistani English. New varieties of English are termed as “there are many recognizable varieties of written and spoken by a large number of people”. No new variety of language is developed in isolation but it is dependent on the people’s communication needs who speak and write it. This kind of variety is known as interference variety because there is interference of culture and language in the culture and first language of the user.

Several changes occur when the people of a language use it in various cultural situation or social context. When the non-native speakers use second language, they develop totally new version of expressions according to the communication requirements. If the bilingual person is the user of non-native variety then the different kinds switching transcription of codes, mixing and alteration are manifested in creativity. When two or more languages get in touch with another it causes the innovation. One of the major means of creativity in language is bilingualism (Talaat, 2003). The non-native verities are widely spread and have stable position that they are regarded as native like English. (Quirk, 1983).

Bilingual Creativity in Pakistani English Newspaper
The stylistics innovation and experimentation has found its peak in literature and journalism. English writing tradition is old before the partition. But in present decades writing is a recognized at a national level. A national award is awarded by a national academy of letters for literature and journalists every year. English press has a large influence in the sub-continent, the reason is that the educated class which is involved in the policy making reads and utilizes it. One can find at least a recognized English newspaper in an average-sized city.

English has become a medium of communication and to convey the message for many years but the cultural aspects are not conveyed in English language. This term is adopted by the news reporter to report the news items. These trends are used for various purposes like irony, cultural meaning and satire. Urdu symbols and metaphors are used regularly and frequently in Pakistani English. These kinds of symbols and metaphors represent the localized behaviours and attitudes and Pakistan social traditions. It is necessary the reader/listener to be familiar with the situation and cultural background to understand the metaphor and the meaning carried by speaker/listener. According to Littlemore (2001) the metaphors are inferred through the knowledge that is shared to a culture because these metaphors are culturally associated.

Rationale of the Study
This study shows that a lot of Urdu and other local words are used in English newspapers. This kind of conversion is introducing a new variety of English in Pakistan and even the vocabulary is changing. The major cause of this changing in vocabulary is the switching of English with local languages of Pakistan. An intensive and detailed study of newspapers indicates that in Pakistani English columns especially in news section localized words are found to a great extent. The comparison of “the News” and “The Dawn” shows the difference between the local and standard variety of English. This research indicates that the emerging trends in English newspaper have a great influence on Pakistani English at words and phrase level. This research shows the varieties of English when it is used by non-native speakers of English. Newspaper is a great source of language learning for students but if the language will not be comprehensible they may get confused and will not be able to learn language properly. So the language of newspaper must be clear and free from slang expressions that are used by Pakistani press. """)

text4 = nlp(u"""from the supernatural premonitions recounted in religious scriptures to Sigmund Freud’s theory of the unconscious, from the simplest bedtime stories we tell our children to the countless sophisticated depictions in literature and cinema, sleep has long beguiled our imagination. Today, journalists and therapists tout the “power of sleep,” while scientists endeavor to unlock the enduring mysteries of an activity that human beings share with fruit flies and sea lions, mice and elephants.

Yet, despite all that has been written on the subject and all the effort devoted to studying the phenomenon scientifically, we do not have a clear answer to a question that would seem to be central to understanding the human experience: “Why do we sleep?”

To answer that we need to first ask what sleep is, and what its essential characteristics are. We know that it is probably evolutionarily conserved, meaning that it has persisted throughout evolutionary history ever since it first evolved. Many scientists also think it is universal among animals, though it has been studied systematically only in a small number of species. Sleep may show up under different guises in different species. Dolphins, for instance, may be able to sleep “unihemispherically” — falling asleep with one half of their brains while the other half remains awake. This allows them to perform complex activities, such as swimming to the surface of the ocean to breathe, without waking up. The nematode worm C. elegans enters into a sleep-like lethargus before molting. In many species, including humans, sleep is generally associated with certain postures, such as lying down, and immobility.

It’s not as easy as you might think to tell if an animal is sleeping. A crude but effective way is to test if an animal is “disconnected” from its environment by providing some stimulation that would typically provoke a strong reaction, such as an unexpected noise. If the animal does not react, there is a good chance that it is genuinely disconnected — and thus sleeping, rather than merely resting. Scientists consider such a reversible disconnection from the environment to be a defining feature of sleep. (An irreversible disconnection from the environment would be a coma.)

Why would animals periodically disconnect from the environment?

One answer offered by biologists is that sleep has no vital function or purpose of its own. This is sometimes called the “null hypothesis” for sleep. Defenders of this view maintain that, unlike eating or reproducing, sleeping is not itself necessary for survival but is useful insofar as it helps animals to avoid predation or to regulate their metabolic rates. Such periods of quiescence may have been naturally selected for because they are conducive to survival by forcing the animal to hide for periods of time. What is essential about sleep, according to this view, is that the animal avoid danger and decreases (temporarily) its use of metabolic resources.

The problem with the null hypothesis is that it has all the hallmarks of a “just-so story.” One could easily turn the reasoning on its head: Doesn’t regularly disconnecting from the environment for a significant portion of time make an organism more vulnerable to predation, not less? Wouldn’t time be better spent on activities that are essential for survival, such as mating, or collecting food or other resources? And if hiding or resting is, evolutionarily speaking, just as good as sleeping, why do so many animals sleep?

If the null hypothesis is wrong, then perhaps sleep does have some essential function.

When I was an undergraduate, a neuroscience professor gave me the following instruction: learn to juggle in a day. I spent the rest of the afternoon, evening, and much of the night in my dorm room trying to figure it out — hours and hours, until finally, closer but still unsuccessful, I crashed into my bed. When I woke up the next morning, I tried again, and lo and behold, I could juggle effortlessly. It felt like magic.

Because of such well-known behavioral effects, neuroscientists have focused on the benefits of sleep for learning and memory. Some speculate that sleep has a special role to play in consolidating and storing memories. One hypothesis is that sleep allows the brain to replay memories in certain structures, such as the hippocampus, thus consolidating those memories. Research on the hippocampus and other regions of the brain, for example the primary visual cortex, suggests that the kind of neural activity that occurs during sleep is in some ways similar to the neural activity that occurred during learning.

However, it’s experimentally difficult to differentiate between a replaying memory and simple background neural activity. Conceptually speaking, it’s like trying to find the shapes of clouds within other clouds. And in any case, replaying memories to consolidate them further hardly seems like the kind of essential function that would explain why sleep is so common, even universal, in the animal kingdom.

Still, learning, memory, and cognitive ability seem to be promising areas for trying to find an essential function of sleep. One recent proposal that attempts to draw these areas together into a single whole is the Synaptic Homeostasis Hypothesis (SHY), originally put forward by Giulio Tononi and Chiara Cirelli in 2003. (Full disclosure: I did my doctoral research in Tononi and Cirelli’s Center for Sleep and Consciousness at the University of Wisconsin–Madison, though SHY was not my focus.)

To my mind, SHY stands apart from other scientific hypotheses about sleep because of its scope and its explanatory elegance. And, despite the fact that elegance is an important feature of scientific theories, there are surprisingly few elegant theories in neuroscience. This may be because so many neuroscientists treat the brain as a modular kludge, focusing on one specific part of the brain as pertaining to their research specifically. SHY, by contrast, is about neural networks in general.

The point of departure for SHY is a refrain that is familiar to all neuroscientists: “neurons that fire together wire together.” This phrase is commonly used to summarize a notion advanced by Donald Hebb in his 1949 The Organization of Behavior. Hebb offered an explanation of what is now called synaptic plasticity — that is, how synapses grow weaker or stronger depending on how often they get used. The core idea is that if neuron A causes neuron B to fire, the next time neuron A fires, it is even more likely to cause neuron B to fire — what is now known as Hebb’s law. It is widely believed that such synaptic plasticity underlies by and large all learning and memory.

But there is a lesser-known implication of the law: If neurons continue firing together, and thus wiring together, creating stronger and stronger connections, then wouldn’t all of the connections eventually become too strong, such that any one neuron could set off a kind of chain reaction through the entire neural network, perhaps even triggering an epileptic fit?

In fact, scientists know that neurons do not always grow stronger through repeated use but can, under the right circumstances, also grow weaker through learning. However, making a neuron fire is more information-rich than keeping a neuron from spiking. So one might expect neural connections to grow stronger generally during learning. An important prediction of SHY is that, on average and over time, neural connections do indeed grow collectively stronger during periods of active learning, which can only occur when an organism is not disconnected from its environment — when it is not sleeping. This means that there is a net increase in synaptic strength during waking hours; the longer you are awake, the stronger your synapses become (generally speaking). It follows that if you were to stay awake long enough, you would run into all sorts of problems: your neurons would saturate, meaning they would no longer be able to acquire new information; the metabolic energy cost of maintaining synapses would become exorbitantly high; and it would become increasingly difficult to respond to neural signals. In short, you would be unable to learn.

SHY proposes that the essential function of sleep is to regulate synapse strength in the brain, allowing us learn during the day. “Sleep is the price the brain pays for plasticity,” as Tononi and Cirelli put it. Specifically, this means that during sleep the synapses are “downscaled” back to the same overall strength they had in their starting state (at the beginning of the day). Maintaining “synaptic homeostasis” in this way keeps synapses from getting too strong, thereby preventing neuron saturation, reducing the amount of metabolic energy the synapses use, and increasing the ratio of neural signals (memories) to noise.

Note that it is the overall strength of the synapses that gets downscaled. It is not as though individual synapses simply revert back to their initial states. That would be counterproductive for learning. Tononi’s and Cirelli’s insight is that what matters for memory is the relative strength of neurons across the entire neural net, not the strength of individual synapses.

If SHY is correct, the reason I woke up able to juggle is that the neural connections from all that repetition were forged before I went to bed. But since the delicate neural connectivity pattern was swamped by the noise of so many other synapses while I was awake, it did not yet translate into a new skill. Sleeping allowed my brain to uncover that connectivity, like sunken architecture being revealed as the tide goes out.

How does the process of downscaling synaptic strength work? We don’t know exactly. There’s some evidence that what are called “slow waves” in deep sleep play an important role. Perhaps slow-wave sleep prunes the overgrown neural garden of the brain. But SHY is neutral as to the precise nature of the neuronal mechanism responsible for downscaling — which, for all we know, might vary across animal species.

Of course, not all scientists who study sleep accept SHY as the best explanation of sleep’s essential function. While SHY is compatible with experimental evidence, much more research is still needed. A potential obstacle is that neuroscientists are often more interested in the local mechanisms of neural activity than the kind of high-level abstractions offered by SHY.

But the very fact that scientists today disagree about why we sleep — why we live out but two-thirds of our lives, and spend the other third disconnected from our environment — is a humbling reminder of how much we still do not know.""")

texts.append(text1)
texts.append(text2)
texts.append(text3)

# best = []
# best.append(ImportentSents(texts, 0))
# best.append(ImportentSents(texts, 1))
# best.append(ImportentSents(texts, 2))



lis = []
d = ss(texts)
for k, v in d.items():
	if v > 0.85:
		lis.append(k)


com_lis = []

lis.reverse()

for v in lis:
	for v2 in lis:
		if v.similarity(v2) > 0.85 and lis.index(v) < lis.index(v2):
			lis.remove(v2)


for v in lis:
	print(v)
	print()

