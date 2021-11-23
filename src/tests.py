import unittest
import mock
from .pokemon import Pokemon, PokeBall, StatusPokemon, TypePokeBall


class PokemonTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.catch_rate = 0.35
        self.pokemon = Pokemon("Pikachu", self.catch_rate)

    def test_poke_ball_master(self):
        poke_ball = PokeBall(TypePokeBall.MASTER_BALL)

        self.pokemon.catch_attempt(poke_ball)

        # Asserts expected
        # Capture guarantee by master ball
        self.assertEqual(self.pokemon.is_caught, True)

        # No changes for catch_rate
        self.assertEqual(self.pokemon.catch_rate, self.catch_rate)

    def test_threshold_less_than_25(self):
        # Set random number N < 25
        with mock.patch('random.randint', return_value=18):
            poke_ball = PokeBall(TypePokeBall.ULTRA_BALL)

            ################################
            # Trying without status
            ################################
            self.pokemon.catch_attempt(poke_ball)

            # Asserts expected
            self.assertEqual(self.pokemon.is_caught, False)
            # Catch rate updated
            self.assertNotEqual(self.pokemon.catch_rate, self.catch_rate)
            updated_catch_rate = self.pokemon.catch_rate

            ################################
            # Now trying with status:ASLEEP
            ################################
            # Set pokemon status
            self.pokemon.set_status(StatusPokemon.ASLEEP)
            self.pokemon.catch_attempt(poke_ball)

            # Asserts expected
            # Now the pokemon was caught
            self.assertEqual(self.pokemon.is_caught, True)

            # No changes for catch_rate
            self.assertEqual(self.pokemon.catch_rate, updated_catch_rate)

            #################################
            # Now trying with status:FROZEN
            #################################
            # Set pokemon status
            self.pokemon.set_status(StatusPokemon.FROZEN)
            self.pokemon.catch_attempt(poke_ball)

            # Asserts expected
            # Now the pokemon was caught
            self.assertEqual(self.pokemon.is_caught, True)
            # No changes for catch_rate
            self.assertEqual(self.pokemon.catch_rate, updated_catch_rate)

    def test_threshold_greater_than_25(self):
        # Set random number N > 25
        with mock.patch('random.randint', return_value=35):
            poke_ball = PokeBall(TypePokeBall.GREAT_BALL)

            ################################
            # Trying without status
            ################################
            self.pokemon.catch_attempt(poke_ball)

            # Asserts expected
            self.assertEqual(self.pokemon.is_caught, False)
            # Catch rate updated
            self.assertNotEqual(self.pokemon.catch_rate, self.catch_rate)
            updated_catch_rate = self.pokemon.catch_rate

            ################################
            # Now trying with status:ASLEEP
            ################################
            # Set pokemon status
            self.pokemon.set_status(StatusPokemon.ASLEEP)
            self.pokemon.catch_attempt(poke_ball)

            # Asserts expected
            # No caught
            self.assertEqual(self.pokemon.is_caught, False)

            # Catch rate updated
            self.assertNotEqual(self.pokemon.catch_rate, updated_catch_rate)
            updated_catch_rate = self.pokemon.catch_rate

            #################################
            # Now trying with status:FROZEN
            #################################
            # Set pokemon status
            self.pokemon.set_status(StatusPokemon.FROZEN)
            self.pokemon.catch_attempt(poke_ball)

            # Asserts expected
            # No caught
            self.assertEqual(self.pokemon.is_caught, False)
            # Catch rate updated
            self.assertNotEqual(self.pokemon.catch_rate, updated_catch_rate)

    def test_threshold_less_than_12(self):
        # Set random number N < 12
        with mock.patch('random.randint', return_value=10):
            poke_ball = PokeBall(TypePokeBall.POKE_BALL)

            ################################
            # Trying without status
            ################################
            self.pokemon.catch_attempt(poke_ball)

            # Asserts expected
            self.assertEqual(self.pokemon.is_caught, False)
            # Catch rate updated
            self.assertNotEqual(self.pokemon.catch_rate, self.catch_rate)
            updated_catch_rate = self.pokemon.catch_rate

            #################################
            # Now trying with status:BURNED
            #################################
            # Set pokemon status
            self.pokemon.set_status(StatusPokemon.BURNED)
            self.pokemon.catch_attempt(poke_ball)

            # Asserts expected
            # Now the pokemon was caught
            self.assertEqual(self.pokemon.is_caught, True)
            # No changes for catch rate
            self.assertEqual(self.pokemon.catch_rate, updated_catch_rate)

            #################################
            # Now trying with status:PARALYZED
            #################################
            # Set pokemon status
            self.pokemon.set_status(StatusPokemon.PARALYZED)
            self.pokemon.catch_attempt(poke_ball)

            # Asserts expected
            # Now the pokemon was caught
            self.assertEqual(self.pokemon.is_caught, True)
            # No changes for catch rate
            self.assertEqual(self.pokemon.catch_rate, updated_catch_rate)

            #################################
            # Now trying with status:POISONED
            #################################
            # Set pokemon status
            self.pokemon.set_status(StatusPokemon.POISONED)
            self.pokemon.catch_attempt(poke_ball)

            # Asserts expected
            # Now the pokemon was caught
            self.assertEqual(self.pokemon.is_caught, True)
            # No changes for catch rate
            self.assertEqual(self.pokemon.catch_rate, updated_catch_rate)

    def test_threshold_greater_than_12(self):
        # Set random number N > 12
        with mock.patch('random.randint', return_value=15):
            poke_ball = PokeBall(TypePokeBall.POKE_BALL)

            ################################
            # Trying without status
            ################################
            self.pokemon.catch_attempt(poke_ball)

            # Asserts expected
            self.assertEqual(self.pokemon.is_caught, False)
            # Catch rate updated
            self.assertNotEqual(self.pokemon.catch_rate, self.catch_rate)
            updated_catch_rate = self.pokemon.catch_rate

            #################################
            # Now trying with status:BURNED
            #################################
            # Set pokemon status
            self.pokemon.set_status(StatusPokemon.BURNED)
            self.pokemon.catch_attempt(poke_ball)

            # Asserts expected
            # No caught
            self.assertEqual(self.pokemon.is_caught, False)
            # Catch rate updated
            self.assertNotEqual(self.pokemon.catch_rate, updated_catch_rate)
            updated_catch_rate = self.pokemon.catch_rate

            #################################
            # Now trying with status:PARALYZED
            #################################
            # Set pokemon status
            self.pokemon.set_status(StatusPokemon.PARALYZED)
            self.pokemon.catch_attempt(poke_ball)

            # Asserts expected
            # No caught
            self.assertEqual(self.pokemon.is_caught, False)
            # Catch rate updated
            self.assertNotEqual(self.pokemon.catch_rate, updated_catch_rate)
            updated_catch_rate = self.pokemon.catch_rate

            #################################
            # Now trying with status:POISONED
            #################################
            # Set pokemon status
            self.pokemon.set_status(StatusPokemon.POISONED)
            self.pokemon.catch_attempt(poke_ball)

            # Asserts expected
            # No caught
            self.assertEqual(self.pokemon.is_caught, False)
            # Catch rate updated
            self.assertNotEqual(self.pokemon.catch_rate, updated_catch_rate)

    def test_change_catch_rate(self):
        self.assertEqual(self.pokemon.catch_rate, self.catch_rate)

        with mock.patch('random.randint', return_value=200):
            poke_ball = PokeBall(TypePokeBall.POKE_BALL)
            self.pokemon.set_catch_rate(poke_ball)

            # Asserts expected
            self.assertEqual(self.pokemon.catch_rate, 0.475)

    def test_str_pokemon(self):
        self.pokemon.set_status(StatusPokemon.FROZEN)
        self.assertEqual(str(self.pokemon), 'Name: Pikachu - Status: FROZEN')

    def test_str_poke_ball(self):
        with mock.patch('random.randint', return_value=18):
            poke_ball = PokeBall(TypePokeBall.POKE_BALL)
            self.assertEqual(str(poke_ball),
                             'Type: POKE_BALL - Associate Random Number: 18')

