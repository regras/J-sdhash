------




# The Jaccard Similarity Digest Hash (JC-sdhash)

	JC-sdhash is a modified version of the Similarity Digest Hash (sdhash) tool [1] that improves both efficiency [2] and quality of the similarity score [3] in comparison to the original version.
	
	When assessing similarity, one needs to create a compact representation for the objects (a.k.a. digest) and then compare theses digests to have a score related to the amount of similar data shared between the two objects. Note that this tool works in the bytewise level to assess similarity.
	
	The code provided here was adapted from sdhash 3.4 (https://github.com/sdhash/sdhash).

------

### INSTALLING JC-sdhash:

	1. Make sure your Operating System has the following tools/libraries installed:
		--> gcc (version 7.4.0)
		--> g++ (version 7.4.0)
		--> make (version 4.1)
		--> make-guile
		--> libssl (libssl-dev)
	
	The dependencies are based on a fresh and updated Ubunutu 18.04.1 installation. Other distributions may require different dependencies.
	
	2. Install PROTOBUF-2.4.1
		--> PROTOBUF is a Google mechanism for serializing structured data, used by JC-sdhash.
		
		--> We recommend using the specific version in attachment to avoid trouble.
		
		--> Basic steps to install Protobuf
			$ ./configure
			$ make
			$ make check
			$ make install
		
		--> Notes:
			--> "make install" may require superuser privileges.
			--> For further instructions on installing protobuf, see its INSTALL.txt file.
			--> The authors say that "If 'make check' fails, you can still install, but it is likely that some features of this library will not work correctly on your system". We have installed with errors and for our purpose, the basic functionalities worked just fine.
	
	3. Install JC-sdhash (for creating the binary only):
		--> $ make
	
	4. Done!
	
	5. Testing the installation process.
		--> To verify if the installation process was performed successfully, use the following commands to create a digest of a test file and compare it to the expected one, using diff command. Both, the file and expected digest, are provided along with JC-sdhash source code, named 'test_file.bin' and 'expected_output.sdbf', respectively. The result of diff should be nothing, which means that both outputs are identical.
		--> command:
			$ JC-sdhash test_file.bin > output.sdbf
			$ diff output.sdbf expected_output.sdbf

------

### USING JC-sdhash

	JC-sdhash works the same way as sdhash. Here, we present a quick and useful set of functions that will be enough for using it.
	
	Most important functions:
		
		1. Creating the digest of a file f:
			$ JC-sdhash f > output.sdbf
	
	where output.sdbf is the name of the file having the digest of f. If no output file is provided, the result is displayed in the system standard output.
		
		2. Comparing the digests of two files f1 and f2:
			$ JC-sdhash f1 > output_f1.sdbf
			$ JC-sdhash f2 > output_f2.sdbf
			$ JC-sdhash -c output_f1.sdbf output_f2.sdbf
		
		3. Creating and comparing the digests of two files f1 and f2 (one command only):
			$ JC-sdhash -g f1 f2
		
		4. Creating the digest of a list of files list_of_files.txt and then comparing it in an all-against-all fashion:
			$ JC-sdhash -f list_files.txt > output_list.sdbf
			$ JC-sdhash -c output_list.sdbf > results.txt
			
	Note that list_of_files.txt should contain the path of each file that will have its similarity assessed, separated by a newline character.
	
	The output of a comparison between two digests using JC-sdhash is shown below:
	
		f1 | f2 | SCORE | JR | JC
		
	where,
		- f1 and f2 are the name of the two objects provided as input for the algorithm.
		- The symbol '|' is a character separation.
		- SCORE is the sdhash result for similarity (to interpret it, see [4], page 13).
		- JR is the Jaccard resemblance score 
			==> JR(A,B)=|A ∩ B| / |A ∪ B|
				where |·| returns the number of elements in the sets. 
		- JC is the Jaccard containment score 
				==> JC(A,B)=|A ∩ B| / |A|, for |B| > |A|
	
	Our results showed that among the three measurements provided, in general, the Jaccard containment (JC) had the best results for describing similarity. When having to choose one of them, we recommend to pick the last one (JC). 

------




### References:

	[1] ROUSSEV, V. Data fingerprinting with similarity digests. In: SPRINGER. IFIP International Conf. on Digital Forensics. [S.l.], 2010. p. 207–226.
	
	[2] KAMEYAMA, A. S.; MOIA, V. H. G.; HENRIQUES, M. A. A. Aperfeiçoamento da ferramenta sdhash para identificação de artefatos similares em investigacoes forenses. In: Extended Anais of XVIII Brazilian Symposium on information and computational systems security. Natal-RN, Brasil: SBC, 2018. p. 223–232. Disponível em: <http://portaldeconteudo.sbc.org.br/index.php/sbseg_estendido/article/view/4161>.
	
	[3] MOIA, V. H. G.; HENRIQUES, M. A. A. Understanding the similarity detected by the sdhash approximate matching function. 2019. IN PREPARATION.
	
	[4] ROUSSEV, V.; QUATES, C. sdhash tutorial: Release 0.8. 2013. <http://roussev.net/sdhash/tutorial/sdhash-tutorial.pdf>. Accessed 2019 Nov 20.

------



