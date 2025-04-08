namespace ChallengeMinesweeper;

// Erreur : Le nom 'Minesweeper' n'existe 
// pas dans le contexte actuel [C:\Projets\dojo-ytreza-dev\minesweeper_challenge_2025\csharp\ChallengeMinesweeper\ChallengeMinesweeper\ChallengeMinesweeper.csproj]

// Action : je dois créer la méthode Minesweeper


public class TestMineSweeper0408Ter
{
    [SetUp]
    public void Setup()
    {
    }

    [TestCase("", "")]
    public void Test1(string unsolvedField, string solvedField)
    {
        Minesweeper(unsolvedField);
    }

    private void Minesweeper(string unsolvedField)
    {
    }
}